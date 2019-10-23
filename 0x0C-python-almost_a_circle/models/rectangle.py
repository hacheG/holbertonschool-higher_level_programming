#!/usr/bin/python3
from models.base import Base
"""begin program - python3"""


class Rectangle(Base):
    """begin program - python3"""

    def __init__(self, width, height, x=0, y=0, id=None):
    	"""begin program - python3"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
    	"""begin program - python3"""
        return self.__width

    @width.setter
    def width(self, width):
    	"""begin program - python3"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
    	"""begin program - python3"""
        return self.__height

    @height.setter
    def height(self, height):
    	"""begin program - python3"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
    	"""begin program - python3"""
        return self.__x

    @x.setter
    def x(self, x):
    	"""begin program - python3"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
    	"""begin program - python3"""
        return self.__y

    @y.setter
    def y(self, y):
    	"""begin program - python3"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
    	"""begin program - python3"""
        return self.__width * self.__height

    def display(self):
    	"""begin program - python3"""
        for space1 in range(self.__y):
            print()
        for row in range(self.__height):
            for space2 in range(self.__x):
                print(" ", end="")

            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
    	"""begin program - python3"""
        a = self.id
        b = self.__x
        c = self.__y
        d = self.__width
        e = self.__height
        f = "[Rectangle]"
        return "{} ({:d}) {:d}/{:d} - {:d}/{:d}".format(f, a, b, c, d, e)

    def update(self, *args, **kwargs):
    	"""begin program - python3"""
        if args:
            newValue = ["id", "width", "height", "x", "y"]
            for count, elem in enumerate(args):
                setattr(self, newValue[count], elem)
        for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
    	"""begin program - python3"""
        dic = {}
        keyVal = vars(self)
        for k, v in keyVal.items():
            dic[k.split("_Rectangle__")[-1]] = v
        return dic
