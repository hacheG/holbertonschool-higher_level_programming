#!/usr/bin/python3
"""

Begin program - python
"""


def number_of_lines(filename=""):
    """
    begin function - number_of_lines
    """
    f = open(filename, 'r')
    for index, line in enumerate(f):
        pass
    return index + 1
