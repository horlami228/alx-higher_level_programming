#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = []
    total = 0
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    for i in new_list:
        total += i
    return total
