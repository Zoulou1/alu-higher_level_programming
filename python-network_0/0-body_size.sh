#!/bin/bash
# This script sends a request to the URL and displays the size of the body of the response in bytes.
curl -s -o /dev/null -w '%{size_download}\n' "$1"
