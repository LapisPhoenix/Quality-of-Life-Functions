def fancy(title:str, content:str, dash_length:int = 20, dash_type:str = "-"):
    """Create fancy formatted information.

    Args:
        title (str): What will be the title EX: ---TITLE---
        content (str): What will be inside the text
        dash_length (int, optional): How many dashes you want for the title, it will adjust with the title length. Defaults to 20.
        dash_type (str, optional): The type of dash EX: ===TITLE=== or @@@TITLE@@@
    """

    FORMAT = dash_type * dash_length + title + dash_type * dash_length

    if len(dash_type) > 1:
      raise Exception("Dash Type must be 1 character long. Example: dash_type='*'")
    else:
        print(f"{FORMAT}\n{content}\n{dash_type * len(FORMAT)}")
