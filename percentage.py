def percentage(a: int, b: int) -> float:
    """
    Calculates the percentage of 2 numbers
    """

    if b == 0:
        return 0.0
    else:
        return round((a / b) * 100, 2)
