#!/usr/bin/python3
""" 0100100100101010010"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.post(argv[1], data={'email': argv[2]})
    print(respo.text)
