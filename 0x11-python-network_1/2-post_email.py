#!/usr/bin/python3
"""
    This scripts takes in a url and email
    sends a POST request and displays the body of the response
    (decoded in utf-8)
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    email = {"email": argv[2]}
    email = urlencode(email).encode("utf-8")
    req = Request(argv[1], email, method="POST")
    with urlopen(req) as response:
        decoded_data = response.read().decode('utf-8')
        print(decoded_data)
