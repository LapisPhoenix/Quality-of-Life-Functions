import colorama


def colorp(level: int, message: str, end: str = '\n'):
    """
    Prints Colored Text
    Arguments:
        level:   int = The message level.
        message: str = The message to display.
        end:     str = The end if the message. (DEFAULT: '\\n')
    Level System:
        0 - Success\n
        1 - Info\n
        2 - Warning\n
        3 - Error\n
        4 - Critical Error\n
    """

    if level not in range(0, 5):
        raise Exception(f"Invalid level {level}. Level has to be between 0-4")

    level_colors = {0: colorama.Fore.LIGHTGREEN_EX,
                    1: colorama.Fore.LIGHTYELLOW_EX,
                    2: colorama.Fore.YELLOW,
                    3: colorama.Fore.LIGHTRED_EX,
                    4: colorama.Fore.RED}

    level_types = {0: "SUCCESS",
                   1: "INFO",
                   2: "WARNING",
                   3: "ERROR",
                   4: "CRITICAL ERROR"}

    if not message:
        raise Exception("Message is a required argument")

    color = level_colors.get(level)
    type = level_types.get(level)
    reset = colorama.Fore.RESET
    print(f"[{color}{type}{reset}] {message}{reset}", end=end)
    return f"[{color}{type}{reset}] {message}{reset}{end}"
