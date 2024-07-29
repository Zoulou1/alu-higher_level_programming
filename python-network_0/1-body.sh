#!/bin/bash
# This script sends a GET request to the URL and displays the body of a 200 status code response.
curl -s -L -w "%{http_code}" "$1" -o response_body && [ "$(cat response_body | tail -c 3)" -eq "200" ] && cat response_body && echo ""
