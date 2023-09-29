#!/bin/bash
# Takes in a URL
curl -s -o /dev/null/ -w "%{size_download}\n" "$1"