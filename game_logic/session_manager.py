import uuid
import time
import logging

# Get a logger object for this module
logger = logging.getLogger(__name__)

class SessionManager:
    def __init__(self):
        self.sessions = {}  # Maps session tokens to Player objects
        self.players_by_name = {}  # Maps player names to Player objects

    def create_session(self, player):
        # Generate a unique session token for the player
        # Store it in the sessions dictionary
        session_token = self.generate_session_token()
        self.sessions[session_token] = player
        player.session_token = session_token
        self.players_by_name[player.name] = player
        return session_token

    def get_player_by_name(self, name):
        return self.players_by_name.get(name)

    def get_player_by_token(self, token):
        return self.sessions.get(token)

    def get_player(self, token):
        # Retrieve the Player object associated with the session token
        return self.sessions.get(token)

    def generate_session_token(self):
        # Generate a unique session token using uuid4
        return str(uuid.uuid4())

    def invalidate_session(self, session_token):
        # Find the player with the given session token
        player = self.sessions.pop(session_token, None)
        if player:
            player.is_connected = False
            # Here you can handle additional cleanup, like saving the player's state

    def handle_disconnection(self, session_token):
        # This method should be called when a disconnection is detected
        player = self.sessions.get(session_token)
        if player:
            player.is_connected = False
            # Remove the session token
            self.sessions.pop(session_token, None)
            # Additional cleanup as necessary

    def get_connected_players(self):
        # Return a list of players who are marked as connected
        return [player for player in self.sessions.values() if player.is_connected]

    def update_last_keepalive(self, session_token):
        # Update the last keepalive time for the session
        if session_token in self.sessions:
            self.sessions[session_token].last_keepalive = time.time()

    def check_keepalives(self):
        # Check for sessions that have missed two consecutive keepalives
        current_time = time.time()
        #logger.info(f"Checking keepalives")
        for session_token, player in list(self.sessions.items()):
            if (current_time - player.last_keepalive) > 60:  # 60 seconds for two keepalives
                self.handle_disconnection(session_token)

session_manager = SessionManager()
