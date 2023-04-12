def number_count(list_to_count):
    """
    Counts how many negatives, positives, and zeros there are in a list and returns each value.
    
    :param list_to_count: The list that'll be used to count how many negatives, positives, and zeros there is.
    
    :return tuple: (positives, negatives, zeros)
    """
    if not isinstance(list_to_count, list):
        raise ValueError("Input must be a list!")
    
    for number in list_to_count:
        if not isinstance(number, int) and not isinstance(number, float):
            raise ValueError("Input must only contain integers and floats!")
    
    positives = len([number for number in list_to_count if number > 0])
    negatives = len([number for number in list_to_count if number <= -1])
    zeros = len([number for number in list_to_count if number == 0])
    
    print(f"Positives: {positives}")
    print(f"Negatives: {negatives}")
    print(f"Zeros: {zeros}")
    
    return (positives, negatives, zeros)
