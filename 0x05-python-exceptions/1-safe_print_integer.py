#!/usr/bin/python3


def safe_print_integer(value):
    """
    This function prints an integer
    :param value: integer
    :return: returns true if value was printed correctly. false for otherwise
    """

    while True:
        try:
            print("{:d}".format(value))
            return True
        except (ValueError, TypeError):
            return False
