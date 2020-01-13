#!/usr/bin/python3
"""01001001010100111110"""

import urllib.request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.getheader("X-Request-Id")
        print(headers)