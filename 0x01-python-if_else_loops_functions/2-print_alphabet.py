#!/usr/bin/python3

# This program prints the alphabet from a to z
for letter in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(letter)), end="")
