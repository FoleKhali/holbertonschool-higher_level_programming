#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """test with integers"""
         self.assertEqual(max_integer([1, 2, 3, 4]), 4)
         self.assertEqual(max_integer([2, 8, 11]), 11)
         self.assertEqual(max_integer([666]), 666)
         self.assertEqual(max_integer([-1, -4, 7]), 7)

    if __name__ == '__main__':
        unittest.main()
