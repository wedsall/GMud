def execute(command, player):
    command_parts = command.split()

    if len(command_parts) < 3:
        return "Invalid command usage. Expected: 'call <object> <property or method>'"

    object_name, attribute = command_parts[1], command_parts[2]

    # Assuming 'here' refers to the current room the player is in
    if object_name == "here":
        current_room = player.get_current_room()
        if current_room:
            # Check if the attribute exists as either a property or a method
            if hasattr(current_room, attribute):
                attr = getattr(current_room, attribute)
                if callable(attr):
                    # If it's a method, call it
                    return str(attr())
                else:
                    # If it's a property, return its value
                    return str(attr)
            else:
                return "Attribute or method not found."
        else:
            return "You are not in any room."

    return "Object not recognized or not accessible."
