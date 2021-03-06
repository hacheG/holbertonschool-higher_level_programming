#!/usr/bin/python3
"""
begin class - Square Class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        begin function - area
        """
        return self.__size * self.__size
