#!/usr/bin/python3

"""
Unittest - python3
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """Unittest - python3"""

    def setUp(self):
        Base.__nb_objects = 0

    def test_00_(self):
        """Unittest - python3"""
        self.assertEqual(Base.__nb_objects, 0)
    
    def test_01_(self):
        b = Base()
        b1 = Base(12)
        self.assertEqual(b.__nb_objects, 0)
        self.assertEqual(b.id, 1)
        self.assertEqual(b.__nb_objects, 0)
        self.assertEqual(b1.id, 12)
        self.assertNotEqual(b.id, 'a')

    def test_02_(self):
        """Test for custom id."""
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_03_(self):
        """Test for no id after a custom entry."""
        b = Base()
        self.assertEqual(b.id, 2)

    def test_04_(self):
        """Test for None input."""
        b = Base(None)
        self.assertEqual(b.id, 3)

    def test_05_(self):
        """Test for zero input."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_06_(self):
        """Test for negative input."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_07_(self):
        """Test for list input."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_08_(self):
        """Test for dict input."""
        b = Base({"hello": "world"})
        self.assertEqual(b.id, {"hello": "world"})

    def test_09_(self):
        """Test for float input."""
        b = Base(9.1)
        self.assertEqual(b.id, 9.1)

    def test_10_(self):
        """Test for tuple input."""
        b = Base((1,))
        self.assertEqual(b.id, (1,))

    def test_11_(self):
        """Test for string input."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_12_(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")
    
    def test_27a_save_to_file_no_args(self):
        """Test for no args in save_to_file."""
        with self.assertRaises(TypeError) as e:
            res = Base.save_to_file()
        self.assertEqual("save_to_file() missing 1 required positional " +
                         "argument: 'list_objs'", str(e.exception))
        
if __name__ == '__main__':
    unittest.main()
