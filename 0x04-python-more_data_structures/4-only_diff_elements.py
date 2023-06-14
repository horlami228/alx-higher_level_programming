#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    i = 0
    selected = list(set_1) + list(set_2)
    for elements in selected:
        if elements in set_2 and elements in set_1:
            del selected[i]
        i += 1

    return selected
