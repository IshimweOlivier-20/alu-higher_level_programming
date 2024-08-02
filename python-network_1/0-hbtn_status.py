#!/usr/bin/python3
"""This script takes a URL as input, sends a request to the given URL,
and displays the value of the 'X-Request-Id' header found in the response."""

import urllib.request

# Define the URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Open the URL and read the response
with urllib.request.urlopen(url) as response:
    headers = response.info()

# Extract and print the 'X-Request-Id' header
request_id = headers.get('X-Request-Id')
print(f'X-Request-Id: {request_id}')
