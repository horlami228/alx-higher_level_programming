#!/usr/bin/pyhton3

# This function prints the last digit of a number


def print_last_digit(number):
    print(f"{abs(number) % 10}", end="")
    return abs(number) % 10
