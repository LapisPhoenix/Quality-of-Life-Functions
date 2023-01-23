import colorama


def colorp(level: int, message: str, end: str = '\n'):
    """
    Prints colored text.
    Arguments:
        level:   int = The message level (0-4).
        message: str = The message to display.
        end:     str = The end of the message (default: '\n').
    Level system:
        0 - Success\n
        1 - Info\n
        2 - Warning\n
        3 - Error\n
        4 - Critical Error\n
    """

    level_colors = {
        0: colorama.Fore.LIGHTGREEN_EX,   # Success
        1: colorama.Fore.LIGHTYELLOW_EX,  # Info
        2: colorama.Fore.YELLOW,          # Warning
        3: colorama.Fore.LIGHTRED_EX,     # Error
        4: colorama.Fore.RED              # Critical Error
    }

    level_types = {
        0: "SUCCESS",
        1: "INFO",
        2: "WARNING",
        3: "ERROR",
        4: "CRITICAL ERROR"
    }

    if level not in level_colors:
        raise ValueError(f"Invalid level {level}. Level must be between 0-4")

    color = level_colors[level]
    type_ = level_types[level]
    reset = colorama.Fore.RESET
    print(f"[{color}{type_}{reset}] {message}{reset}", end=end)

    if level == 4:
        exit(message)
