import grpc
import mud_pb2
import mud_pb2_grpc
import threading
import time
import readline
from getpass import getpass

def run():
    # Establish a gRPC channel and create a stub for the MudService
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mud_pb2_grpc.MudServiceStub(channel)

        # Placeholder for any authentication mechanism you might want to implement
        username = input("Enter your username: ")
        password = getpass("Enter your password: ")

        response = stub.Login(mud_pb2.LoginRequest(name=username, password=password))
        if response.success:
            print("Login successful.")
            session_token = response.session_id  # Store the session token
            # Start the keepalive thread here
            keepalive_thread = threading.Thread(target=send_keepalive, args=(stub, session_token))
            keepalive_thread.daemon = True
            keepalive_thread.start()

            listen_thread = threading.Thread(target=listen_for_messages, args=(stub, username))
            listen_thread.start()

            print(f"Session {session_token}")
        else:
            print("Login failed.")
            return

        # Main loop to send commands
        print("Connected to the MUD server. Type 'quit' to exit.")

        while True:
            command = input("> ")

            readline.add_history(command)
            try:
                # Send the command to the servera
                metadata=[('session-token', session_token)]
                response = stub.ExecuteCommand(mud_pb2.CommandRequest(command=command), metadata=metadata)
                # Print the result from the server
                print(response.result)
            except grpc.RpcError as e:
                print(f"An error occurred: {e.details()}")

def send_keepalive(stub, session_id):
    while True:
        try:
            stub.KeepAlive(mud_pb2.KeepAliveRequest(session_id=session_id))
            #print("Keepalive sent")
        except grpc.RpcError as e:
            print(f"An error occurred while sending keepalive: {e.details()}")
        time.sleep(30)  # Send a keepalive every 30 seconds

def listen_for_messages(stub, player_id):
    for response in stub.StreamMessages(mud_pb2.StreamMessagesRequest(player_id=player_id)):
        print(response.message)

if __name__ == '__main__':
    run()
