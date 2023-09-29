#!/usr/bin/env bash
# Takes in a URL
# sends a request to it
# displa the size of the response body in bytes

curl -s -o /dev/null/ -w "%{size_download}\n" $1

