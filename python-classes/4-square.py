#!/usr/bin/python3
# 4-square.py
# 6005@holbertonstudents.com
"""Access and update private attribute"""


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
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Returns the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
