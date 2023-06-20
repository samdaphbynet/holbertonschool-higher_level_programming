#!/usr/bin/python3
# Filename: 10-square.py
"""
This file contains the difinition of the Square class.
that inherits from the Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a square instance
        Args:
            size: size of the Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
