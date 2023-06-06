#!/usr/bin/python3

# This function checks if a letter is lower case or upper case


def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
