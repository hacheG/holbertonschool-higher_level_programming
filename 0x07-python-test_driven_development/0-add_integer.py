#!/usr/bin/python3
"""
   Function that return the addition of two numbers
"""


def add_integer(a, b=98):
	 """
    Args:
         a: integer or float
         b: integer or float
    Raises:
         TypeError: a must be an integer
         TypeError: b must be an integer
    Returns:
         Addition of two numbers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
    	raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)     
        return a + b
 