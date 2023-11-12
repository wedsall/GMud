import grpc
from concurrent import futures
import importlib
import logging
import os
import sys
import time
import threading
import mud_pb2
import mud_pb2_grpc
from collections import defaultdict
import queue
from game_logic.item import Item
from game_logic.player import Player
from game_logic.game_world import game_world
from game_logic.session_manager import session_manager
from game_logic.command_parser import command_parser

# Set up logging
logging.basicConfig(level=logging.INFO)

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# In the server class, you would initialize a SessionManager instance
class MudService(mud_pb2_grpc.MudServiceServicer):
    def __init__(self):
        self.session_manager = session_manager
        self.command_parser = command_parser
        game_world.set_mud_service(self)
        self.message_queues = defaultdict(queue.Queue)
        self.message_available = defaultdict(threading.Event)
        keepalive_check_thread = threading.Thread(target=periodic_keepalive_check, args=(self.session_manager,))
        keepalive_check_thread.daemon = True
        keepalive_check_thread.start()

    def Login(self, request, context):
        existing_player = self.session_manager.get_player_by_name(request.name)

        if existing_player:
                # Reconnect the existing player
                existing_player.is_connected = True
                session_id = self.session_manager.create_session(existing_player)
                # Return the existing player's session
                return mud_pb2.LoginResponse(success=True, message="Reconnected to existing player.", session_id=session_id)
        else:
            # If the player doesn't exist, create a new one
            default_room = game_world.load_room('rooms/starting_room.lua')
            new_player = Player(request.name, default_room)
            new_player.is_connected = True
            session_id = self.session_manager.create_session(new_player)
            game_world.add_player(new_player)
            return mud_pb2.LoginResponse(success=True, message="New player created.", session_id=session_id)
        
    def Logout(self, request, context):
        # Extract the session token from the metadata
        metadata = dict(context.invocation_metadata())
        session_token = metadata.get('session-token')

        # Use the token to get the player object
        player = self.session_manager.get_player_by_token(session_token)
        if player:
            player.is_connected = False
            # Handle additional logout logic, such as saving the player state
            return mud_pb2.LogoutResponse(success=True, message="Logged out successfully.")
        else:
            return mud_pb2.LogoutResponse(success=False, message="No active session found.")

    def StreamMessages(self, request, context):
        player_id = request.player_id
        while context.is_active():
            # Wait until a message is available or a timeout occurs
            message_event = self.message_available[player_id]
            message_event.wait(timeout=1)
            while not self.message_queues[player_id].empty():
                message = self.message_queues[player_id].get()
                yield mud_pb2.StreamMessagesResponse(message=message)
            message_event.clear()

    def ExecuteCommand(self, request, context):
        metadata = dict(context.invocation_metadata())
        session_token = metadata.get('session-token')
        
        # Use CommandParser to execute the command
        result = self.command_parser.execute_command(request.command, session_token)

        # Return the result as the command response
        return mud_pb2.CommandResponse(result=result)

    def KeepAlive(self, request, context):
        # Update the last keepalive time for the session
        #logging.exception(f"Keepalive received from {request.session_id}")
        self.session_manager.update_last_keepalive(request.session_id)
        return mud_pb2.KeepAliveResponse(success=True)

    def send_message_to_player(self, player_name, message):
        self.message_queues[player_name].put(message)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mud_pb2_grpc.add_MudServiceServicer_to_server(MudService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()

def periodic_keepalive_check(session_manager):
    while True:
        #logging.info("Checking keepalives..")
        session_manager.check_keepalives()
        time.sleep(30)  # Check every 30 seconds

if __name__ == '__main__':
    serve()

