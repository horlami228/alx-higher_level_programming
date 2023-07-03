#!/usr/bin/python3

"""create a Rectangle Class"""


class Rectangle:
    """This defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object

        :param width: Rectangle object width
        :param height: Rectangle object height
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Retrieve the value of an attribute
        :param self: object or instance of a class
        :return: returns the value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set or update the value of an attribute

        :param value: attribute value
        :return: The correct input value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the value of an attribute
        :param self: object or instance of a class
        :return: returns the value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set or update the value of an attribute

        :param value: attribute value
        :return: The correct input value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of the Triangle object
        :return: area value
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate and return the perimeter value
        :return: perimeter value
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        This function returns a string representation of the object Rectangle

        :return: returns a string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = []
            for i in range(self.__height):
                rectangle.append("#" * self.__width)
                rectangle.append("\n")
            return "".join(rectangle)
