#!/usr/bin/python3
import urllib.request

urls = ["https://intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]

for url in urls:
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print(f"Fetching {url}")
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
    print()
