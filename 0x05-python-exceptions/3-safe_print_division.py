#!/usr/bin/python3

# This function divides two integers
# catch and handle any error that may occur
# use the try/except/finally block


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
