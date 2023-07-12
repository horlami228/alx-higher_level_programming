#!/usr/bin/python3
"""
We can return a list of attributes, methods and even inherited magic methods
of a class
"""


def lookup(obj):
    """
    This function returns a list of all attributes and methods
    by a class
    :param obj: The class object
    :return: A list
    """
    return dir(obj)
