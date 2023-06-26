#!/usr/bin/python3
import sys

# This function executes a function safely
# we can use fct as a pointer to a function
# *args as variable number of arguments for the function
# return result of function. otherwise None if error occurred
# print error to stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
