import importlib
import logging
import os
from game_logic.session_manager import session_manager
from game_logic.game_world import game_world
from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)
logger = logging.getLogger(__name__)

class CommandParser:
    def __init__(self):
        self.session_manager = session_manager

    def execute_command(self, command_text, session_token):
        # Retrieve the player based on the session token
        player = self.session_manager.get_player(session_token)
        if not player:
            return "Invalid session token or player not found."

        # Parse the command to get the command name
        command_name = command_text.split(' ')[0]

        # Step 2: Check commands/ directory
        command_module = self.check_command_directory(command_name)
        if command_module:
            return self.execute_directory_command(command_module, command_text, player)

        # Step 3: Check emotes/ directory
        lua_emote=self.check_emotes_directory(command_name)
        if lua_emote:
            return self.execute_emote_command(player, lua_emote, command_name)

        # Step 5: Check room exits
        if player.current_room and command_name in player.current_room.exits:
            return self.handle_room_exit(player, command_name)

        return "What?"

    def check_emotes_directory(self, emote_name):
        emote_path = f'emotes/{emote_name}.lua'

        # Check if the emote file exists
        if os.path.exists(emote_path):  
            # Load the emote script
            with open(emote_path, 'r') as file:
                lua_script = file.read()
                return lua_script
        return False
 
    def execute_emote_command(self, player, lua_emote, target_name):
        emote = lua.execute(lua_emote)
        current_room = player.current_room

        # Call the execute function from the emote with player and target names
        playerName = player.name
        targetName = ''
        player_msg, target_msg, others_msg = emote['execute'](playerName)
        game_world.tell_player(player.name, player_msg)
        game_world.tell_room(current_room, others_msg, exclude_players=[player])     

    def handle_room_exit(self, player, direction):

        current_room = player.current_room
        exit_path = current_room.get_exit(direction)
        if exit_path:
            # Load the destination room using the Lua script path
            players_to_exclude = [player]
            game_world.tell_room(current_room, f"{player.cap_name()} leaves {direction}.", exclude_players=players_to_exclude)
            new_room = game_world.load_room(exit_path)
            player.move_to_room(new_room)
            new_desc = player.get_current_room().get_description('', player)
            game_world.tell_room(player.get_current_room(), f"{player.cap_name()} arrives.", exclude_players=players_to_exclude)

            return f"You move {direction}.\n{new_desc}"
        else:
            return "You can't go that way."        


    def check_command_directory(self, command_name):

        # Dynamically import the module for the command
        try:
            command_module = importlib.import_module(f'commands.{command_name}')
        except ModuleNotFoundError:
            return False
        return command_module

    def execute_directory_command(self, command_module, command_text, player):

        # Execute the command with the player object
        try:
            return command_module.execute(command_text, player)
        except Exception as e:
            # Log the error and return a failure message
            logger.exception("An error occurred while executing the command.")
            return f"Error executing command: {e}"

command_parser = CommandParser()
