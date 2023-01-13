#!/usr/bin/python3
"""define a class Rectangle"""


class Rectangle:
    """represent a Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):

        """"initialize a new retangle instance
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        Returns:
            return the value. True for success. false for otherwise
        """

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """control the input for width
        Args:
            value(int): width value
        """
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
        """control the input for height
        Args:
            value(int): height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """"returns the area value"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter value"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return (str(self.print_symbol) *
                    self.__width + "\n") * self.__height

    def __repr__(self):
        """returns a representation of a rectangle instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """return a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
