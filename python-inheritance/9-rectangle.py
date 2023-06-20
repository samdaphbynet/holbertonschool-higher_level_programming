#!/usr/bin/python3
# NameFile: 8-rectangle.py
"""
This class Rectangle that inherits from BaseGeometry.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The Rectangle class inherits from the BaseGeometry class.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ returns a string representation of the Rectangle instance.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
