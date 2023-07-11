#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a file using JSON
    :param my_obj: object to convert to JSON
    :param filename: File name
    :return: return the string representation in a textfile
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
