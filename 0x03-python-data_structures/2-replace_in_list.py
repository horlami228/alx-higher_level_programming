#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """This function replaces element in a list"""
    if idx < 0:
        return None
    elif idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
