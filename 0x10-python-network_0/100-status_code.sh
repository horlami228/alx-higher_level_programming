#!/bin/bash
# display status code from request
curl -s -o /dev/null/ -w "%{http_code}\n" "$1"
