#!/usr/bin/python3
def add_integer(a, b=98):
    if a != type(int) and b != type(int):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        return a + b
 
