#!/usr/bin/python3
"""
This function writes a string to a text file
"""

def write_file(filename="", text=""):
    """
    This function write a string to a text file
    :param filename: name of file
    :param text: string to be written in file
    :return: number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
