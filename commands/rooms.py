# Assuming the GameWorld instance is accessible from this module
from game_logic.game_world import game_world

def execute(command, player):
    # Initialize an empty list to store room info strings
    rooms_info = []

    # Iterate through the dictionary of loaded rooms
    for lua_path, room in game_world.world_rooms.items():
        # Compile the room information into a string
        room_info = f"Lua Path: {lua_path}, Name: {room.name}"
        rooms_info.append(room_info)

    # Join all room information strings with a newline character for readability
    rooms_list = "\n".join(rooms_info)

    # Check if the list is empty and return appropriate message
    if rooms_list:
        return rooms_list
    else:
        return "No rooms are currently loaded."

