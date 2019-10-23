#!/usr/bin/python3
from models.rectangle import Rectangle
"""begin program - python3"""


class Square(Rectangle):
	"""begin program - python3"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
    	"""begin program - python3"""
        a = self.id
        b = self.x
        c = self.y
        d = self.width
        f = "[Square]"
        return "{} ({}) {}/{} - {}".format(f, a, b, c, d)

    @property
    def size(self):
    	"""begin program - python3"""
        return self.width

    @size.setter
    def size(self, size):
    	"""begin program - python3"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
    	"""begin program - python3"""
        if args:
            newValue = ["id", "size", "x", "y"]
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
