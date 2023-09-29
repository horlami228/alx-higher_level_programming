#!/usr/bin/python3

"""
    sends a request to a URL and
    displays the value of the variable
    X-Request-Id
"""

import requests
from sys import argv

if __name__ == "__main__":
    fetch_detail = requests.get(argv[1])
    print(fetch_detail.headers["X-Request-Id"])
