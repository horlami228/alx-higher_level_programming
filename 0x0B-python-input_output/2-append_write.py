#!/usr/bin/python3
"""
This function appends a string to the end of file
"""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of file
    :param filename: File name
    :param text: The text to append
    :return: returns with an appended text
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
