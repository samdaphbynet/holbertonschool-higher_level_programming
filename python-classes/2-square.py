#!/usr/bin/python3
# 2-square.py
# 6005@holbertonstudents.com
"""Size validation"""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The private size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square with the given size.
        Args:
            size (int, optional): The size of the square. Default is 0.
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
