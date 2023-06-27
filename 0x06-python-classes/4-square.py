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
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the value
        :return: Returns the correct output
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        set the correct input
        :param value: object size instance value
        :return: return true for success. 0 for otherwise
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculate the area of the square
        :return: returns the area of the square
        """
        return self.__size ** 2
