def execute(command, player):

    # Assuming the player object has an attribute 'session_token'
    if player and hasattr(player, 'session_token'):
        return f"Your session token is: {player.session_token}"
    else:
        return "You are not currently logged in with a valid session."

