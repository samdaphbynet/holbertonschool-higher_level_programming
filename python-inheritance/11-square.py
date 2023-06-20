#!/usr/bin/python3
# Filename: 11-square.py
"""
This class Rectangle that inherits from BaseGeometry class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The Square class inherits from Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a square instance
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        __str__ returns a string representation of the square instance.
        """
        return f"[Square] {self.__size}/{self.__size}"
