#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """This function prints all integers in a list
    in reverse order"""

    last = len(my_list) - 1
    while last >= 0:
        print("{}".format(my_list[last]))
        last -= 1
