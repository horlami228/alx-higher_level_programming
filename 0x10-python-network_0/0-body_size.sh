#!/bin/bash
# Takes in a URL

curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
