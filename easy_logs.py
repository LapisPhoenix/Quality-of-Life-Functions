"""
Create simple log files with error handling.
Example Log: 29/11/2022 18:12:18 :: #tickets purged by Lapis Pheonix#2194\
You can edit the message, divider, and if you want to write to a file.
"""

from datetime import datetime

def log(message:str, divider:str = "::", write_to_file:bool = True):
    """Logs a message to the console and optionally to a file.

    Args:
        message (str): What will be printed to the console and optionally written to a file.
        divider (_type_, optional): What seperates the time and message. Defaults to "::".
        write_to_file (bool, optional): If you want to write to a file or not,  defaults to True.
    """
    
    try:
        now = datetime.now()
    except Exception as e:
        raise Exception(f"Failed to get the current time.\nCaught error: {e}")
    DATE_FORMAT = "%d/%m/%Y %H:%M:%S"  # Edit this to desired format
    
    print(f"{now.strftime(DATE_FORMAT)} {divider} {message}")
    
    if write_to_file:
        with open("log.txt", "a") as log:
            log.write(f"{now.strftime(DATE_FORMAT)} {divider} {message}\n")
    else:
        return message
