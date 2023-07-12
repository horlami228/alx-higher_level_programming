#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Inherited from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Define a Rectangle object
    """

    def __init__(self, width, height):
        """
        Initializing a new Rectangle object
        :param width: Rectangle width
        :param height: Rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
