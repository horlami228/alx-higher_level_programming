#!/usr/bin/python3

"""
We want to return true if the object is exactly an instance
of a class
"""


def is_same_class(obj, a_class):
    """
    This function checks if an object is the
    :param obj: class instance
    :param a_class: object class
    :return: True
    """
    return type(obj) is a_class
