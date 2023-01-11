#!/usr/bin/python3


class Rectangle:
    """define a rectangle class"""

    def __init__(self, width=0, height=0):
        """"initialize a class retangle
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieve the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """control the input for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """control the input for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
