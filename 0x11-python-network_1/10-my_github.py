#!/usr/bin/python3

"""
    This python script takes GitHub
    credentials (username and password(Token))
    We are going to use the GitHub API to display the id
"""

import requests
from sys import argv

username = str(argv[1])
password = str(argv[2])

get_headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer {}".format(password),
    "X-Github-Api-Version": "2022-11-28"
}

url = "https://api.github.com/users/{}".format(username)
req = requests.get(url, headers=get_headers, allow_redirects=True)
try:
    req_json = req.json()
    print(req_json["id"])
except Exception:
    print(None)
