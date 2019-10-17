#!/usr/bin/python3
"""
Begin program - python
"""


def read_lines(filename="", nb_lines=0):
    """
    begin function - read_lines
    """
    l = []
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            if index < nb_lines or nb_lines == 0:
                l.append(line)
            else:
                break
        print("{}".format("".join(l)), end="")
