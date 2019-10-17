#!/usr/bin/python3
"""
Begin program - python
"""


def read_file(filename=""):
    """
    begin function - read_file
    """
    f = open(filename, 'r')
    for line in f:
        print('{}'.format(line), end='')
