#!/usr/bin/python3


class Square():
    """Class Square with setter & getter"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        if not isinstance(x, int):
            raise TypeError("size must be an integer")
        if x < 0:
            raise ValueError("size must be >= 0")

        self.__size = x

    def area(self):
        return (self.__size * self.__size)

    def __lt__(self, other):
        """Override the default Equals behavior"""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the default Equals behavior"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the default Equals behavior"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Override the default Equals behavior"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the default Equals behavior"""
        return self.area() >= other.area()
