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

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
