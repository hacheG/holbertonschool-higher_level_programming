#!/usr/bin/python3
"""bla bla bla"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    theMail = argv[2]
    data = parse.urlencode({'email': theMail}).encode()

    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
