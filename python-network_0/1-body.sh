#!/bin/bash
# This script sends a GET request to the URL and displays the body of a 200 status code response.
curl -sL -o /dev/stderr -w "%{http_code}" "$1" 2> response_body | [ "$(tail -n 1 response_body)" = "200" ] && head -n -1 response_body
