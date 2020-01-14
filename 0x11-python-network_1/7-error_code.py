#!/usr/bin/python3
""" 0000000101111111111101010"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    if resp.status_code > 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
