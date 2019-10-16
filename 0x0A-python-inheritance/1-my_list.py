#!/usr/bin/python3
"""
a function in python
"""


class MyList(list):
    """
    begin class - MyList
    """
    def print_sorted(self):
        """
        begin function - print_sorted
        """
        print("{}".format(sorted(self)))