from game_logic.session_manager import session_manager

def execute(command, player):
    # This command does not need the player object, but it's passed for consistency
    connected_players = session_manager.get_connected_players()
    if connected_players:
        player_names = [player.name for player in connected_players]
        return "Connected players: " + ", ".join(player_names)
    else:
        return "No players are currently connected."

