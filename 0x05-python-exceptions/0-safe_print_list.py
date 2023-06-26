#!/usr/bin/python3

# This function prints X elements in a list


def safe_print_list(my_list=[], x=0):
    """
    Args:
        my_list(list): List we are working with
        x(int): number of elements to print
    Returns: my_list if successful
    """
    i = 0
    while True:
        try:
            if i < x:
                print("{}".format(my_list[i]), end="")
                i += 1
            else:
                print()
                return i
        except IndexError:
            print()
            return i
