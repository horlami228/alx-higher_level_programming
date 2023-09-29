#!/usr/bin/python3

"""
    takes in a URL and email address
    sends a POST request with the email as parameter
    display the reponse body
"""

import requests
from sys import argv

if __name__ == "__main__":

    email = {"email": argv[2]}
    post = requests.post(argv[1], data=email)
    print(post.text)
