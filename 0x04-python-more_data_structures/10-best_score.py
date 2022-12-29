#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    great = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value is great:
            return key
