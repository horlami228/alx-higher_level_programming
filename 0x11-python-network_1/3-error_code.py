#!/usr/bin/python3

"""
    handle exception and print error code
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            decoded_data = response.read().decode("utf-8")
            print(decoded_data)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
