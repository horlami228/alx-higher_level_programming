#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure
    :param obj: instance object of a class
    :return: Returns a dictionary
    """
    dic = {}
    for keys, values in obj.__dict__.items():
        if isinstance(values, (int, list, dict, str, bool)):
            dic[keys] = values
    return dic
