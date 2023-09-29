#!/bin/bash
# display status code from request
curl -sI -o /dev/null/ -w "%{http_code}\n" "$1"
