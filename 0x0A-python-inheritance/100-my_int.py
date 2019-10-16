#!/usr/bin/python3
"""
begin program - python
"""


class MyInt(int):
    def __eq__(self, y):
        if self <= y and self >= y:
            return False
        return True

    def __ne__(self, y):
        if self > y or self < y:
            return False
        return True