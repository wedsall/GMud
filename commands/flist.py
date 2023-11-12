def execute(command, player):
    command_parts = command.split()

    # Ensure there is at least one part: the object name
    if len(command_parts) < 2:
        return "Invalid command usage. Expected: 'list <object>'"

    object_name = command_parts[1]

    # Assuming 'here' refers to the current room the player is in
    if object_name == "here":
        current_room = player.get_current_room()
        if current_room:
            attrs_methods = dir(current_room)
            # Filter out special methods and attributes (those starting and ending with __)
            filtered_attrs_methods = [am for am in attrs_methods if not am.startswith('__') and not am.endswith('__')]
            return ', '.join(filtered_attrs_methods)
        else:
            return "You are not in any room."

    return "Object not recognized or not accessible."
