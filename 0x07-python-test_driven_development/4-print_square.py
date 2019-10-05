#!/usr/bin/python3
"""
   Function that prints a square depending of the size parameter
"""


def print_square(size):
     """
    Args:
        size: integer number
    Raises:
       TypeError: size must be an integer
       ValueError: size must be >= 0
    Returns:
       the square printed using #
    """
    msnError1 = "size must be an integer"
    msnError2 = "size must be >= 0"

    if not type(size) == int:
        raise TypeError(msnError1)

    if size < 0:
       	raise ValueError(msnError2)

    if isinstance(size, float) and size < 0:
      	raise ValueError(msnError1)
        
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
