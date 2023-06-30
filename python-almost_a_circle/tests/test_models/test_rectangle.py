#!/usr/bin.python3
"""
    Module of test of subclass Rectangle
"""

import unittest
from pathlib import Path
import os
import io
import sys
from models.base import Base
from models.rectangle import Rectangle

class Test_Rectangle_attribut(unittest.TestCase):

    def test__widthType(self):
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.width) is int)

    def test__heightType(self):
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.height) is int)

    def test__xType(self):
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.x) is int)

    def test__yType(self):
        rect1 = Rectangle(2, 8, 1, 2)
        self.assertTrue(type(rect1.y) is int)


class Test_Rectangle_attributRaise(unittest.TestCase):

    def test__widthTypeError(self):
        with self.assertRaises(TypeError)as e:
            rect2 = Rectangle('2', 8, 1, 2)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test__widthValueError(self):
        with self.assertRaises(ValueError) as e:
            rect3 = Rectangle(-2, 8, 0, 0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test__widthValueError(self):
        with self.assertRaises(ValueError) as e:
            rect3 = Rectangle(0, 8, 0, 0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test__heightTypeError(self):
        with self.assertRaises(TypeError) as e:
            rect4 = Rectangle(2, '8', 0, 0)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test__heightValueError(self):
        with self.assertRaises(ValueError) as e:
            rect4 = Rectangle(2, -8, 0, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test__heightValueError(self):
        with self.assertRaises(ValueError) as e:
            rect4 = Rectangle(2, 0, 0, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test__xTypeError(self):
        with self.assertRaises(TypeError) as e:
            rect5 = Rectangle(2, 8, "8", 0)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test__yTypeError(self):
        with self.assertRaises(TypeError) as e:
            rect6 = Rectangle(2, 8, 0, "5")
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test__xValueError(self):
        with self.assertRaises(ValueError) as e:
            rect7 = Rectangle(2, 8, -2, 0)
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test__yValueError(self):
        with self.assertRaises(ValueError) as e:
            rect8 = Rectangle(2, 8, 2, -10)
        self.assertEqual(str(e.exception), 'y must be >= 0')


class Test_Rectangle_method(unittest.TestCase):

    @staticmethod
    def captureOutput(rect, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return (capture)

    def test_area(self):
        rect9 = Rectangle(2, 3)
        self.assertEqual(Rectangle.area(rect9), 6)

    def test_str(self):
        rect10 = Rectangle(2, 3, 0, 5, 8)
        self.assertEqual(Rectangle.__str__(rect10),
                         "[Rectangle] (8) 0/5 - 2/3")

    def test_RectangleDisplayWithoutXY(self):
        rect11 = Rectangle(1, 2)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("#\n#\n", capture.getvalue())
        self.assertEqual(rect11.x, 0)
        self.assertEqual(rect11.y, 0)

    def test_RectangleDisplayZeroXY(self):
        rect = Rectangle(3, 2, 0, 0)
        capture = Test_Rectangle_method.captureOutput(rect, "display")
        self.assertEqual('###\n###\n', capture.getvalue())

    def test_RectangleDisplayXonly(self):
        rect11 = Rectangle(1, 2, 4)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("    #\n    #\n", capture.getvalue())

    def test_RectangleDisplayYonly(self):
        rect11 = Rectangle(1, 2, 0, 1)
        capture = Test_Rectangle_method.captureOutput(rect11, "display")
        self.assertEqual("\n#\n#\n", capture.getvalue())
    
    def test_RectangleDisplayOneArg(self):
        rect11 = Rectangle(1, 2, 0, 1)
        with self.assertRaises(TypeError):
            rect11.display(12)

    def test_toDictionaryOutput(self):
        rect12 = Rectangle(8, 2, 1, 9, 5)
        answer = {'width': 8, 'height': 2, 'x': 1, 'y': 9, 'id': 5}
        self.assertDictEqual(answer, rect12.to_dictionary())

    def test_uptdateOneArg(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54)
        self.assertEqual("[Rectangle] (54) 1/1 - 1/1", str(rect13))

    def test_uptdateTwoArg(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12)
        self.assertEqual("[Rectangle] (54) 1/1 - 12/1", str(rect13))

    def test_uptdateThreeArg(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24)
        self.assertEqual("[Rectangle] (54) 1/1 - 12/24", str(rect13))

    def test_uptdateForArg(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24, 8)
        self.assertEqual("[Rectangle] (54) 8/1 - 12/24", str(rect13))

    def test_uptdateFiveArg(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(54, 12, 24, 8, 5)
        self.assertEqual("[Rectangle] (54) 8/5 - 12/24", str(rect13))

    def test_uptdateOneKwargs(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{"width": 2})
        self.assertEqual("[Rectangle] (1) 1/1 - 2/1", str(rect13))

    def test_uptdateTwoKwargs(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'height': 24})
        self.assertEqual("[Rectangle] (1) 1/1 - 2/24", str(rect13))

    def test_uptdateThreeKwargs(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 1/1 - 2/24", str(rect13))

    def test_uptdateForKwargs(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'width': 2, 'x': 16, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 16/1 - 2/24", str(rect13))

    def test_uptdateFiveKwargs(self):
        rect13 = Rectangle(1, 1, 1, 1, 1)
        rect13.update(**{'y': 2, 'width': 2, 'x': 16, 'height': 24, 'id': 48})
        self.assertEqual("[Rectangle] (48) 16/2 - 2/24", str(rect13))


class Test_Base_Create(unittest.TestCase):

    def test_createRectangle(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(rect14))

    def test_createRectangleNew(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertEqual("[Rectangle] (14) 14/14 - 14/14", str(rect15))

    def test_createRectangleDiffFirst(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertIsNot(rect15, rect14)

    def test_createRectangleNotEqualFirst(self):
        rect14 = Rectangle(14, 14, 14, 14, 14)
        rect14_dict = rect14.to_dictionary()
        rect15 = Rectangle.create(**rect14_dict)
        self.assertNotEqual(rect15, rect14)

class Test_Base_MethodeWithFile(unittest.TestCase):

    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_RectangleSaveToFileNone(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertTrue("[]", file.read())

    def test_RectangleSaveToFile_none(self):
        self.assertEqual(Rectangle.save_to_file(None), None)

    def test_RectangleSaveToFileEmpty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertTrue("[]", file.read())

    def test_RectangleSaveToFile_empty(self):
        self.assertEqual(Rectangle.save_to_file([]), None)

    def test_OneRectangleSaveToFile(self):
        rect16 = Rectangle(12, 6, 2, 4, 8)
        Rectangle.save_to_file([rect16])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_TwoRectangleSaveToFile(self):
        rect16 = Rectangle(12, 6, 2, 4, 8)
        rect17 = Rectangle(24, 48, 16, 8, 25)
        Rectangle.save_to_file([rect16, rect17])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 109)

    def test_NoArgSaveToFile(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_RectangleLoadFromFileNoFile(self):
        answer = Rectangle.load_from_file()
        path = Path('Rectangle.json')
        self.assertFalse(path.is_file())

    def test_RectangleLoadFromFileExistFile(self):
        rect18 = Rectangle(12, 6, 2, 4, 54)
        rect19 = Rectangle(48, 16, 8, 25, 78)
        Rectangle.save_to_file([rect18, rect19])
        answer = Rectangle.load_from_file()
        self.assertTrue(all(type(form)) == Rectangle for form in answer)


if __name__ == '__main__':
    unittest.main()