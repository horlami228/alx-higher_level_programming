#!/usr/bin/python3

"""define a class BaseGeometry"""


class BaseGeometry:
    """define a class BaseGeometry"""
    def area(self):
        """
        Raise an exception
        :return: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value
        :param name: A string
        :param value: An integer
        :return: None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
