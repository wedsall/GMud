from game_logic.session_manager import session_manager

def execute(command, player):
    # Mark the player as not connected
    player.is_connected = False

    # Invalidate the player's session
    session_manager.invalidate_session(player.session_token)

    # Return a message indicating the player has been disconnected
    return "You have been disconnected from the game."

