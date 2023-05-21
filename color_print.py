import sys
import colorama
from enum import Enum


class Logger:

    class Level(Enum):
        SUCCESS = 0
        INFO = 1
        WARNING = 2
        ERROR = 3
        CRITICAL_ERROR = 4

    def colorp(self, level: int, message: str, end: str = '\n'):
        """
        # Prints color logs to the console.

        ## Parameters
        ---
        - level: int
            - The level of the log.
        - message: str
            - The message to be printed.
        - end: str
            - The end character to be used when printing the message.
        
        ## Returns
        ---
        - None

        ## Raises
        ---
        - ValueError
            - If the level is not between 0-4.
        
        ## Example
        ---
        ```py
        from utils.logging import Logger

        logger = Logger()

        logger.colorp(Logger.Level.SUCCESS, "This is a success message.")
        ```
        """

        colorama.init()

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
            sys.exit(message)
