#!/usr/bin/python3

# This function executes a function safely
# we can use fct as a pointer to a function
# *args as variable number of arguments for the function
# return result of function. otherwise None if error occurred
# print error to stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as exe:
        print("Exception:", str(exe))
        return None
