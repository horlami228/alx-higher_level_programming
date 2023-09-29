#!/usr/bin/python3

"""
    handle exception and print error code
"""
from sys import argv
import requests


if __name__ == "__main__":
    fetch = requests.get(argv[1])
    if fetch.status_code < 400:
        print(fetch.status_code)
    else:
        print("Error code {}".format(fetch.status_code))
