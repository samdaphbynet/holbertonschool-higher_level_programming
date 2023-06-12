#!/usr/bin/python3
# 1-square.py
# 6005@holbertonstudants.com
"""Square class"""


class Square:
    """square for generation function"""
    def __init__(self, size):
        """
        Initialize square instance.
        args:
        size (int): size of square
        attributes:
        __size (int): the private instance attribute representing size square
        """
        self.__size = size
