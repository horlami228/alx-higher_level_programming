#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file
    :param filename: File name
    :return: An object
    """
    with open(filename, mode="r", encoding="utf-8") as file:

        return json.load(file)
