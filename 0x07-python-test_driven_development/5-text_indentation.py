#!/usr/bin/python3


def text_indentation(text):
    """
    This function prints a string and for every occurrence
    of this characters('.', '?', ':') it prints two new lines
    :param text: string value
    :return: A string
    """

    special_char = ["?", ".", ":"]

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # split text into lines that is stored in a list
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        for char in special_char:
            line = line.replace(char, char + "\n\n")
        print(line)
