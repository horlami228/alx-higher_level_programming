#!/usr/bin/python3

"""create a Rectangle Class"""


class Rectangle:
    """This defines a rectangle class"""
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle object

        :param width: Rectangle object width
        :param height: Rectangle object height
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
                rectangle.append(str(self.print_symbol) * self.__width)
                rectangle.append("\n")
            return "".join(rectangle)

    def __repr__(self):
        """
        It provides an unambiguous representation of an object

        :return: a string representation of the Rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """

        This method deletes an object
        :return: return a string after deletion
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This function calculates and returns the biggest rectangle based
        on the area

        :param rect_1: rectangle object 1
        :param rect_2: rectangle object 2
        :return: The rectangle object with the biggest area or object 1 if
                they are equal
        """

        # check if both object are instances of the class Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect-2 must be an instance of Rectangle")

        # check and return the biggest Rectangle object

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
