#!/usr/bin/python3
def print_square(size):
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
