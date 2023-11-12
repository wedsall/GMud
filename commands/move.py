from game_logic.game_world import game_world

def execute(command, player):
    # The command string would be something like "move east"
    direction = command.split()[1]  # The second word is the direction

    current_room = player.current_room
    exit_path = current_room.get_exit(direction)
    if exit_path:
        # Load the destination room using the Lua script path
        new_room = game_world.load_room(exit_path)
        player.move_to_room(new_room)
        new_desc = player.get_current_room().get_description()

        return f"You move {direction}.\n{new_desc}"
    else:
        return "You can't go that way."

