#!/usr/bin/python3


def print_square(size):
    """
    The square function prints a square
    with "#"

    :param size: Width and Height of the square
    :return: return a "#" square format
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # print the square
    for i in range(size):
        print("#" * size)
