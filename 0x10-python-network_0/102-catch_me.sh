#!/bin/bash
# make a request to the server and the 0.0.0.0:5000/catch_me response with You got me!
curl -sX PUT -d "user_id=98" -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me"
