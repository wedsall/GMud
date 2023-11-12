-- Define the starting room
starting_room = {
    name = "Office Room",
    description = "A small, cozy office with a desk and a chair.",
    exits = {
        east = "rooms/room2.lua",
        north = "rooms/room3.lua"
    },
    items = {
        {
            names = {"phone", "telephone"},
            description = "It's a phone!"
        },
        {
            names = {"book", "novel"},
            description = "A gripping adventure novel."
        },
    },
    monsters = {
    {
        path = "monsters/dragon.lua",
        params = {name = "Ancient Dragon", health = 200, attack_power = 50},
        count = 1
    },
    {
        path = "monsters/goblin.lua",
        params = {name = "Goblin", health = 30, attack_power = 5},
        count = 3 
    }
}
}

-- Return the room
return starting_room

