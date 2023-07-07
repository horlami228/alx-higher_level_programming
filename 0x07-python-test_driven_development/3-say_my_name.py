#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    This function prints the first_name and last_name

    :param first_name: First parameter
    :param last_name: Second parameter
    :return: Returns a string with both first and last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
