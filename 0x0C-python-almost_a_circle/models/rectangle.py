#!/usr/bin/python3
"""define a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """This class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiate a new object Rectangle
        :param width: width of the Rectangle
        :param height: Height of the Rectangle
        :param x: X value
        :param y: Y value
        :param id: Object ID
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting the private instance attribute
        :param value: width value
        :return: width
        """
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """
        Getter method
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting the private instance attribute
        :param value: height value
        :return: height
        """

        self.validation("height", value)

        self.__height = value

    @property
    def x(self):
        """
        Getter method
        :return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting the private instance attribute
        :param value: x value
        :return: x
        """

        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Getter method
        :return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting the private instance attribute
        :param value: y value
        :return: y
        """

        self.validation("y", value)
        self.__y = value

    @staticmethod
    def validation(attribute, value):
        """
        This static method is used for setter validation
        :param attribute: Attribute name
        :param value: Attribute value
        :return: value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """
        This public method returns the area of the rectanlge
        :return: Area (width * height)
        """
        return self.__width * self.__height

    def display(self):
        """
        Display Rectangle with #
        :return: visual Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        for j in range(self.__y):
            print(" ")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        prints a string representation of Rectangle
        :return: A string
        """
        return f"[{type(self).__name__}] ({self.id}) " \
               f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        This method can be used to update the attributes
        :param args: Variable optional arguments
        """
        tab = 0
        if args and len(args) != 0:
            for arg in args:
                if tab == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if tab == 1:
                    self.__width = arg
                if tab == 2:
                    self.__height = arg
                if tab == 3:
                    self.__x = arg
                if tab == 4:
                    self.__y = arg
                tab += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        This method returns a dictionary representation
        of the object
        :return: A dictionary
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
