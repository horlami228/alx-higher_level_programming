#!/usr/bin/python3

# This program prints 1 to 99 with each number separated by a comma and space
for num in range(0, 100):
    if num == 99:
        print("{:d}".format(num))
    else:
        print("{:02}".format(num), end=", ")
