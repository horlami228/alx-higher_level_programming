#!/usr/bin/python3

# This program prints the alphabet in reverse and alternates lowercase
# to uppercase
i = 1
for letter in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        letter = letter - 32
        print("{}".format(chr(letter)), end="")
    else:
        print("{}".format(chr(letter)), end="")
    i += 1
