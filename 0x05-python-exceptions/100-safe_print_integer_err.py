#!/usr/bin/python3

# print only integers
# The argument can contain any value
# return true if successful. otherwise false
# print exception error to stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except(TypeError, ValueError) as exe:
        print("Exception: {}".format(str(exe)))
        return False
