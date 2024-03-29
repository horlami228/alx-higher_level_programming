#!/usr/bin/python3

"""
   This script takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    letter = {"q": q}
    req = requests.post("http://0.0.0.0:5000/search_user", data=letter)
    try:
        req = req.json()
        id, name = req.get("id"), req.get("name")
        if len(req) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except ValueError:
        print("Not a valid JSON")
