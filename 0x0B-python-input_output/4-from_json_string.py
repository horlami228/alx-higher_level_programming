#!/usr/bin/python3
"""
This function converts a JSON string back to an object
"""
import json


def from_json_string(my_str):
    """
    This function converts a JSON string back to an object
    :param my_str: JSON string
    :return: object of the string representation
    """

    return json.loads(my_str)
