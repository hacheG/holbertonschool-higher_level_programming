#!/usr/bin/python3
"""ldsijfhilWFHILSHADLF"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    print(resp.headers.get('X-Request-Id'))
