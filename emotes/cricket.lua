-- Define the 'cricket' emote
return {
    execute = function(playerName, targetName)
        local playerMessage, targetMessage, othersMessage

        if targetName then
            -- If targetName is provided, include it in the messages
            playerMessage = "You listen to crickets chirping with " .. targetName .. "."
            targetMessage = playerName .. " listens to crickets chirping with you."
            othersMessage = playerName .. " listens to crickets chirping with " .. targetName .. "."
        else
            -- If targetName is nil, modify the messages to exclude it
            playerMessage = "You listen to the crickets chirping."
            -- targetMessage is not needed as there is no target
            targetMessage = ""
            othersMessage = playerName .. " listens to the crickets chirping."
        end

        return playerMessage, targetMessage, othersMessage
    end
}

