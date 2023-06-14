#!/usr/bin/python3

# replaces all occurrences of an element by another in a new list.


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    i = 0
    for num in new_list:
        if num == search:
            new_list[i] = replace
        i += 1
    return new_list
