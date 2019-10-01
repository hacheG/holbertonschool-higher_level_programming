#!/usr/bin/python3


class Square():
    """Class Square with position"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, x):
        if not str(x).isdigit():
            raise TypeError("size must be an integer")
        if x < 0:
            raise ValueError("size must be >= 0")

        self.__size = x

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
