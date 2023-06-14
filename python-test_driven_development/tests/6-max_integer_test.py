#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
Unittest for max_integer([..])
Test when the list is empty
Test when the list contains positive numbers
Test when the list contains negative numbers
Test when the list contains both positive and negative numbers
Test when the list contains duplicate numbers
"""


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_positive_num(self):
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_max_integer_negative_num(self):
        result = max_integer([-1, -1, -3])
        self.assertEqual(result, -1)

    def test_max_integer_dup_num(self):
        result = max_integer([1, 3, 2, 3])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
