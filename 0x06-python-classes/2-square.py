#!/usr/bin/python3
"""define a square class"""


class Square:
    def __init__(self, size=0):
        """initialize with a private instance size
        and an optional argument"""
        if not isinstance(size, int):
            """check if size is int"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """if size < 0"""
            raise ValueError("size must be >= 0")
        self.__size = size
