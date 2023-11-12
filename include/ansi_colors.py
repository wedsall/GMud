class ANSI:
    # Normal Foreground Colors
    FG_BLACK = "\033[30m"
    FG_RED = "\033[31m"
    FG_GREEN = "\033[32m"
    FG_YELLOW = "\033[33m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_WHITE = "\033[37m"

    # Bold/Bright Foreground Colors
    FG_BLACK_BOLD = "\033[1;30m"
    FG_RED_BOLD = "\033[1;31m"
    FG_GREEN_BOLD = "\033[1;32m"
    FG_YELLOW_BOLD = "\033[1;33m"
    FG_BLUE_BOLD = "\033[1;34m"
    FG_MAGENTA_BOLD = "\033[1;35m"
    FG_CYAN_BOLD = "\033[1;36m"
    FG_WHITE_BOLD = "\033[1;37m"

    # Normal Background Colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Bold/Bright Background Colors
    BG_BLACK_BOLD = "\033[1;40m"
    BG_RED_BOLD = "\033[1;41m"
    BG_GREEN_BOLD = "\033[1;42m"
    BG_YELLOW_BOLD = "\033[1;43m"
    BG_BLUE_BOLD = "\033[1;44m"
    BG_MAGENTA_BOLD = "\033[1;45m"
    BG_CYAN_BOLD = "\033[1;46m"
    BG_WHITE_BOLD = "\033[1;47m"

    RESET = "\033[0m"
# Usage
#from ansi_colors import ANSIColors
#print(f"{ANSIColors.FG_RED}Red foreground{ANSIColors.RESET} and {ANSIColors.BG_GREEN}green background{ANSIColors.RESET}")

