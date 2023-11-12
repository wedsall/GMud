-- Define the 'hmm' emote
return {
    execute = function(playerName, targetName)
        local playerMessage = "You go 'hmm'."
        local othersMessage = playerName .. " goes 'hmm'."

        return playerMessage, nil, othersMessage
    end
}
