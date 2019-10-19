#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
	"""begin program - python3"""

	def __init__(self, width, height, x=0, y=0, id=None):
		super().__init__(id)
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y

		@property
		def width(self):
			return self.__width

		@width.setter
		def width(self, width):
			self.__width = width

		@property
		def heigth(self):
			return self.__height

		@heigth.setter
		def heigth(self, heigth):
			self.__height = heigth

		@property
		def x(self):
			return self.__x

		@x.setter
		def x(self, x):
			self.__x = x

		@property
		def y(self):
			return self.__y

		@y.setter
		def y(self, y):
			self.__y = y