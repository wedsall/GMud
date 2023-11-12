from include.ansi_colors import ANSI
from game_logic.game_world import game_world

def execute(command, player):
    # Extract the message from the command
    # Assuming the command is in the format "say <message>"
    _, _, message = command.partition(' ')  # Split the command from the message

    if not message:
        return "What do you want to say?"

    # Broadcast the message to the room
    room = player.current_room
    if room:
        game_world.tell_room(room, f"{ANSI.FG_YELLOW}{player.cap_name()} says: {message}{ANSI.RESET}", exclude_players=[player])

        return f"{ANSI.FG_YELLOW}You say: {message}{ANSI.RESET}"
    else:
        return "You are not in a room."

