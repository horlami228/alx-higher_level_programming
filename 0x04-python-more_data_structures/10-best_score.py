#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    biggest_key = ""
    great_num = 0
    for keys, values in a_dictionary.items():
        if values > great_num:
            great_num = values
            biggest_key = keys
    return biggest_key
