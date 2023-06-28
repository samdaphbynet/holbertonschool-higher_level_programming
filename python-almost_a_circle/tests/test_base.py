import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_from_json_string(self):
        json_string = '[]'
        self.assertEqual(Base.from_json_string(json_string), [])
        json_string = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(json_string), [{"id": 1}])

    def test_create(self):
        r1 = Rectangle(1, 2)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)
        self.assertEqual(r1, r2)

        s1 = Square(3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)
        self.assertEqual(s1, s2)

    def test_load_from_file(self):
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Rectangle.load_from_file(), [])
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        rectangles = [r1, r2]
        Rectangle.save_to_file(rectangles)
        rectangles_loaded = Rectangle.load_from_file()
        self.assertIsInstance(rectangles_loaded, list)
        self.assertEqual(len(rectangles_loaded), 2)
        self.assertIsInstance(rectangles_loaded[0], Rectangle)
        self.assertIsInstance(rectangles_loaded[1], Rectangle)
        self.assertEqual(rectangles_loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(rectangles_loaded[1].to_dictionary(), r2.to_dictionary())

        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Square.load_from_file(), [])
        s1 = Square(3)
        s2 = Square(4)
        squares = [s1, s2]
        Square.save_to_file(squares)
        squares_loaded = Square.load_from_file()
        self.assertIsInstance(squares_loaded, list)
        self.assertEqual(len(squares_loaded), 2)
        self.assertIsInstance(squares_loaded[0], Square)
        self.assertIsInstance(squares_loaded[1], Square)
        self.assertEqual(squares_loaded[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(squares_loaded[1].to_dictionary(), s2.to_dictionary())

    def test_save_to_file(self):
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        rectangles = [Rectangle(1, 2), Rectangle(3, 4)]
        Rectangle.save_to_file(rectangles)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, '
                                       '{"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}]')

        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        squares = [Square(3), Square(4)]
        Square.save_to_file(squares)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            contents = file.read()
            self.assertEqual(contents, '[{"id": 1, "size": 3, "x": 0, "y": 0}, '
                                       '{"id": 2, "size": 4, "x": 0, "y": 0}]')

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        json_string = Base.to_json_string([{"id": 1}])
        self.assertEqual(json_string, '[{"id": 1}]')
        self.assertIsInstance(json_string, str)


if __name__ == '__main__':
    unittest.main()
