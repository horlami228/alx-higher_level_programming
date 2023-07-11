#!/usr/bin/python3
import json
"""
This function converts a python object to a JSON string
"""

def to_json_string(my_obj):
    """
    This function converts a python object to a JSON string
    :param my_obj: python object
    :return: A JSON string
    """

    return json.dumps(my_obj)
