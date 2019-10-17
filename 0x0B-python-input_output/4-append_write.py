#!/usr/bin/python3
"""
Begin program - python
"""


def append_write(filename="", text=""):
    """
    begin function - append_write
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        return f.write(text)
