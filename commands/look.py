def execute(command, player):
    if player and player.get_current_room():
        room = player.get_current_room()

        # Split the command to check if there's a specific target
        parts = command.split()
        if len(parts) > 2 and parts[1].lower() == "at":
            # Target specified in the command
            target = " ".join(parts[2:])

            # First, check if the target is one of the room's contents
            description = room.get_object_description(target)
            if description:
                return description

            # Next, check for the target among the room's items
            # Assuming there's a method in Room to get an item's description
            item_description = room.get_item_description(target)
            if item_description:
                return item_description

            return f"There is no '{target}' here."
        else:
            # No specific target, return the general description of the room
            return room.get_description(player)
    else:
        return "You are not in any room."

