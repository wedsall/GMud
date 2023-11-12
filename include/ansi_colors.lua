ANSI = {
    -- Normal Foreground Colors
    FG_BLACK = "\27[30m",
    FG_RED = "\27[31m",
    FG_GREEN = "\27[32m",
    FG_YELLOW = "\27[33m",
    FG_BLUE = "\27[34m",
    FG_MAGENTA = "\27[35m",
    FG_CYAN = "\27[36m",
    FG_WHITE = "\27[37m",

    -- Bold/Bright Foreground Colors
    FG_BLACK_BOLD = "\27[1;30m",
    FG_RED_BOLD = "\27[1;31m",
    FG_GREEN_BOLD = "\27[1;32m",
    FG_YELLOW_BOLD = "\27[1;33m",
    FG_BLUE_BOLD = "\27[1;34m",
    FG_MAGENTA_BOLD = "\27[1;35m",
    FG_CYAN_BOLD = "\27[1;36m",
    FG_WHITE_BOLD = "\27[1;37m",

    -- Normal Background Colors
    BG_BLACK = "\27[40m",
    BG_RED = "\27[41m",
    BG_GREEN = "\27[42m",
    BG_YELLOW = "\27[43m",
    BG_BLUE = "\27[44m",
    BG_MAGENTA = "\27[45m",
    BG_CYAN = "\27[46m",
    BG_WHITE = "\27[47m",

    -- Bold/Bright Background Colors
    BG_BLACK_BOLD = "\27[1;40m",
    BG_RED_BOLD = "\27[1;41m",
    BG_GREEN_BOLD = "\27[1;42m",
    BG_YELLOW_BOLD = "\27[1;43m",
    BG_BLUE_BOLD = "\27[1;44m",
    BG_MAGENTA_BOLD = "\27[1;45m",
    BG_CYAN_BOLD = "\27[1;46m",
    BG_WHITE_BOLD = "\27[1;47m",

    RESET = "\27[0m"
-- Example
-- print(ANSIColors.FG_RED .. "Red foreground" .. ANSIColors.RESET .. " and " .. ANSIColors.BG_GREEN .. "green background" .. ANSIColors.RESET)

