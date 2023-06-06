#!/usr/bin/python3

# This program prints all possible different combination of two digits
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
