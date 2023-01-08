#!/usr/bin/python3
"""define a class square"""


class Square:
    """represent a squre"""
    def __init__(self, size=0):
        """initialize a new square instance

        Args:
            size(int): size of the squre
        Returns:
            The return value. true for success. otherwise for false
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Args:
            size(int): size of the square
        Returns:
            The square area
        """
        return self.__size * self.__size
