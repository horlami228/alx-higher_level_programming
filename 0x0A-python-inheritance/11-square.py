#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
"""
This Square class inherits from the Rectangle class
"""


class Square(Rectangle):
    """define a square class"""

    def __init__(self, size):
        """
        Initialize a new square object
        :param size: Square size
        """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Return a string representation for the class
        :return: A string
        """
        return f"[Square] {self.__size}/{self.__size}"
