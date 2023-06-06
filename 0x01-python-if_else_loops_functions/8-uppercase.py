#!/usr/bin/python3

# This function prints a string in uppercase


def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print()
