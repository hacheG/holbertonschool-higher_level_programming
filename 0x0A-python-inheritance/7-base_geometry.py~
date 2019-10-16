#!/usr/bin/python3
"""
Begin program python
"""


class BaseGeometry:
    """
    Begin class - BaseGeometry
    """
    def area(self):
        """
        Begin fuction - area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        begin function - integer_validator
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))