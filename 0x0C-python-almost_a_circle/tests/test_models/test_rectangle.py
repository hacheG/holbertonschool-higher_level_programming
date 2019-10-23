#!/usr/bin/python3

"""
Unittest - python3
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base

class RectangleTest(unittest.TestCase):
    """Unittest - python3"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_01_two_args(self):
        """Test for two arguments passed in."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_02_three_args(self):
        """Test for three arguments passed in."""
        r = Rectangle(98, 12, 64)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 98)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 64)
        self.assertEqual(r.y, 0)

    def test_03_four_args(self):
        """Test for four arguments passed in."""
        r = Rectangle(4, 51, 96, 88)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 51)
        self.assertEqual(r.x, 96)
        self.assertEqual(r.y, 88)

    def test_04_five_args(self):
        """Test for five arguments passed in."""
        r = Rectangle(5, 66, 151, 44, 822)
        self.assertEqual(r.id, 822)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 66)
        self.assertEqual(r.x, 151)
        self.assertEqual(r.y, 44)

if __name__ == '__main__':
    unittest.main()
