#!/usr/bin/python3
"""define a class square"""


class Square:
    """create a square instance"""

    def __init__(self, size=0):
        """initialize a square insance

        Args:
            size(int): size of the square
        Returns:
            return a value. true for success. false otherwise.
        """

        self.__size = size

    @property
    def size(self):
        """Returns the current size"""
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
        """returns the current square area"""

        return self.__size * self.__size

    def my_print(self):
        """ prints to stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
