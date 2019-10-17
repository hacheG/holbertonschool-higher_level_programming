#!/usr/bin/python3
"""
Begin program - python
"""
import json


def load_from_json_file(filename):
    """
    begin function - load a json object
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        text = f.read()
        return json.loads(text)
