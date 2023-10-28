# Ascii Logger

import string


def ascii_log(title: str, content: str, dash_length: int = 20, dash_symbol: str = "-") -> None
    """
    Log information in a neat format:
    
    ---TITLE---\n
    CONTENTS\n
    -----------
    :param title: What is shown at the top of the log
    :param content: Whats inside the log
    :param dash_length: How many symbols to print for title bar
    :param dash_symbol: The symbol to use as the title bar
    :return: None
    """
    if len(dash_symbol) != 1:
        raise IndexError("Dash Symbol must be 1 character long. Example: dash_symbol='-'")

    TITLE_BAR = f"{dash_symbol * dash_length}{title}{dash_symbol * dash_length}"
    offset = 0

    if dash_symbol not in [*string.ascii_letters, *string.digits, *string.punctuation]:
        offset = 2

    print(f"{TITLE_BAR}\n{content}\n{dash_symbol * (len(TITLE_BAR) - offset)}")
