#!/usr/bin/python3
"""This script takes a URL as input, sends a request to the given URL,
and displays the value of the 'X-Request-Id' header found in the response."""

import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
