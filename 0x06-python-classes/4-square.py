#!/usr/bin/python3
"""define a class square"""


class Square:

    """represent a square"""

    def __init__(self, size=0):
        """Initialize a new square instance
        Args:
            size(int): size of the square
        Returns:
            Return the value. True for sucess. false for otherwise
        """
        self.__size = size

    @property
    def size(self):
        """set current size for square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value(int): size variable
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get the area for the square"""
        return self.__size * self.__size
