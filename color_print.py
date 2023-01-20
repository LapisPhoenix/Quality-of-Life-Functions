import colorama


def colorp(level: int, message: str, end: str = '\n'):
    """
    Prints Colored Text

    Arguments:
        level:   int = The message level.
        message: str = The message to display.
        end:     str = The end if the message. (DEFAULT: '\n')

    Level System:
        1 - Info
        2 - Warning
        3 - Error
        4 - Critical Error
    """

    if level not in range(1, 5):
        raise Exception(f"Invalid level {level}. Level has to be between 1-4")

    level_colors = {1: colorama.Fore.LIGHTYELLOW_EX,
                    2: colorama.Fore.YELLOW,
                    3: colorama.Fore.LIGHTRED_EX,
                    4: colorama.Fore.RED}

    level_types = {1: "INFO",
                   2: "WARNING",
                   3: "ERROR",
                   4: "CRITICAL ERROR"}

    if not message:
        raise Exception("Message is a required argument")

    color = level_colors.get(level)
    type = level_types.get(level)
    reset = colorama.Fore.RESET
    print(f"[{color}{type}{reset}] {message}{reset}", end=end)
