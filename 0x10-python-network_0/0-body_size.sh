#!/usr/bin/env bash
# Takes in a URL
# sends a request to it
# displa the size of the response body in bytes

curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
