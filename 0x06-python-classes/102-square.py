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

    def __eq__(self, other):
        """initialize a equal comparison == method"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __lt__(self, other):
        """initialize a less than < method"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """initialize a less than or equal <= method"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """initialize a greater than > method"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """initialize a greater than or equal >= method"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __ne__(self, other):
        """initialize a not equal to != method"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return False
