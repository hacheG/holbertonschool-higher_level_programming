#!/usr/bin/python3
"""000111111100000111010101"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://swapi.co/api/people/"
    params = {"search": argv[1]}
    resp = requests.get(url, params=params)
    try:
        data = resp.json()
        print("Number of results:", data.get("count"))
        for result in data.get("results"):
            print(result.get("name"))
    except ValueError:
        print("Not a valid JSON")
