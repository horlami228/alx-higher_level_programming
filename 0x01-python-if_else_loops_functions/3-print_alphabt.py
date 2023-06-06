#!/usr/bin/python3

# This program prints the alphabet from a to z except the letter q and e
for letter in range(ord('a'), ord('z') + 1):
    if letter == ord('e') or letter == ord('q'):
        continue
    else:
        print("{}".format(chr(letter)), end="")
