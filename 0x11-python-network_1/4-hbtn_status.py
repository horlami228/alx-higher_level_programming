#!/usr/bin/python3

"""
    fetches from a url with the package requests
"""
import requests

if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")
    print(fetch.text)
    print("Body response:")
    print(f"\t- type: {type(fetch.text)}")
    print(f"\t- content: {fetch.text}")
