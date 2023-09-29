#!/usr/bin/python3
"""
    This scripts takes in a url and display the header value
    of X-Request-Id
"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        with urlopen(url) as response:
            print(response.headers["X-Request-Id"])
    else:
        pass
