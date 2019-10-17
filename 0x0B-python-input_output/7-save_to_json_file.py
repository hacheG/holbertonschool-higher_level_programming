#!/usr/bin/python3
"""
Begin program - python
"""
import json


def save_to_json_file(my_obj, filename):
    """
    begin function -  Save a json
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(json.dumps(my_obj))
