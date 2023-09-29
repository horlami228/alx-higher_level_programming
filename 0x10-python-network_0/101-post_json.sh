#!/bin/bash
# post request from a json file to a URL
curl -sX POST -d "$(cat "$2")" -H "Content-Type: application/json" "$1"
