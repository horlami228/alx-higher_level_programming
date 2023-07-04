#!/usr/bin/python3


def add_integer(a, b=98):
    """
    This function adds and returns two integers

    :param a: First operand
    :param b: Second operand
    :return: The addition of both values
    """
    # check if a and b are integers or floats

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
