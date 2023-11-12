-- Define the dragon
local function create_dragon(params)
    return {
        name = params.name,
        health = params.health,
        attack_power = params.attack_power
        -- Add more properties and behaviors as needed
    }
end

return create_dragon
