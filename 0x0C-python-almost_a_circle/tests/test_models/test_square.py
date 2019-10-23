#!/usr/bin/python3

"""
Unittest - python3
"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

class SquareTest(unittest.TestCase):
    """Unittest - python3"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00_one_arg(self):
        """Test for one argument passed in."""
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_01_two_args(self):
        """Test for two arguments passed in."""
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_02_three_args(self):
        """Test for three arguments passed in."""
        r2 = Square(98, 12, 64)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 98)
        self.assertEqual(r2.x, 12)
        self.assertEqual(r2.y, 64)

    def test_03_four_args(self):
        """Test for four arguments passed in."""
        r3 = Square(4, 51, 96, 88)
        self.assertEqual(r3.id, 88)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 51)
        self.assertEqual(r3.y, 96)

if __name__ == '__main__':
    unittest.main()