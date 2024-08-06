#!/usr/bin/python3
"""
This module fetches the status from two URLs:
- https://intranet.hbtn.io/status
- http://0.0.0.0:5050/status
"""

import urllib.request

def fetch_status(url):
    """Fetches and prints the status from a given URL."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
    print(f"Fetching {url}")
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
    print()

if __name__ == "__main__":
    for url in ["https://intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]:
        fetch_status(url)
