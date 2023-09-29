#!/usr/bin/python3

"""
    fetches from a url with the package requests
"""
import requests

if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")
    print(fetch.text)
    print("Body response:")
    print("\t- type: {}".format(type(fetch.text)))
    print("\t- content: {}".format(fetch.text))
