#!/usr/bin/python3
"""
    defines a square class
"""


class Square:
    """
        Represent a square class
    """

    def __init__(self, size=0):
        """initialize with a private instance size
        and an optional argument

        Args:
            size(int): The size of new square
        Returns:
            The return value. true for success, false for otherwise
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the square area
        :return: Returns the square area
        """
        return self.__size ** 2
