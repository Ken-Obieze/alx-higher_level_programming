#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me to get the message "You got me!".
curl -sLH -X PUT  "Origin: School" -d "user_id=98" 0:5000/catch_me
