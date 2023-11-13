-- Define the starting room
starting_room = {
    name = "Starting Room 3",
    description = "A small, dimly lit room that serves as the beginning of your adventure.",
    exits = {
        south = "rooms/starting_room.lua"
        -- Add other exits as needed
    }
}

-- Return the room
return starting_room

