#!/usr/bin/python3
from urllib.request import urlopen
from pprint import pprint
"""
    This python script fetches from a url and
    display the response
"""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        fetch_details = response.read()
        print("Body response:")
        print("   - type: {}".format(type(fetch_details)))
        print("   - content: {}".format(fetch_details))
        print("   - utf8 content: {}".format(response.msg))
