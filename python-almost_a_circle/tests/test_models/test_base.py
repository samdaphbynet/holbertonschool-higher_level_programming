#!/usr/bin.python3
"""
    Module of test
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.base = Base(12)

    def test_nb_objects(self):
        Base.__nb_objects = 0

    def test_ID(self):
        base = Base(39)
        self.assertEqual(base.id, 39)

    def test_IDNone(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)


class TestBaseStaticMethod(unittest.TestCase):

    def setUp(self):
        self.base = Base(12)

    def test_outputTypeToJsonString(self):
        list_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(type(Base.to_json_string(list_dict)), str)

    def test_outputEmptyToJsonString(self):
        list_dict = None
        self.assertEqual(Base.to_json_string(list_dict), '[]')

    def test_outputTypeFromJsonString(self):
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(type(Base.from_json_string(json_string)), list)

    def test_outputEmptyTypeFromJsonString(self):
        json_string = None
        self.assertEqual(Base.from_json_string(json_string), [])


if __name__ == '__main__':
    unittest.main()