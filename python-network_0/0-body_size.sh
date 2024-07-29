#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL,
# and displays the size of the body of the response in bytes.

if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Send a request to the URL and display the size of the response body in bytes
curl -s -o /dev/null -w '%{size_download}\n' "$URL"
