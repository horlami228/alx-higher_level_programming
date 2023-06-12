#!/usr/bin/python3


def no_c(my_string):
    """This function removes all characters c and C in a string"""
    new_string = ""
    for letter in my_string:
        if letter not in ["c", "C"]:
            new_string += letter

    return new_string
