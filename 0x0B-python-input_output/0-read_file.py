#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """
    This function reads a file and prints it out
    :param filename: The name of the file
    :return: The data in the file
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
