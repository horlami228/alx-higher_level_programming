#!/usr/bin/python3

"""
   This script takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv
import json

if __name__ == "__main__":
    if len(argv) == 1:
        print("No result")
    else:
        letter = {"q": argv[1]}
        req = requests.post("http://0.0.0.0:5000/search_user", data=letter)
        response_body = req.text
        data = json.loads(response_body)
        if len(data) != 0:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
