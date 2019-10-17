#!/usr/bin/python3
"""
Begin program - python
"""


def write_file(filename="", text=""):
    """
    begin function - write_file
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        return f.write(text)
