#!/usr/bin/python3
import sys

# print only integers
# The argument can contain any value
# return true if successful. otherwise false
# print exception error to stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]))
        return False
