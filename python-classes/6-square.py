#!/usr/bin/python3
# 5-square.py
# 6005@holbertonstudents.com
"""Coordinates of a square"""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The private size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size.
        args:
            size (int, optional): the size of the square. Defaults to 0.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates and returns the area of the square
        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        Calculates and returns the position of the square
        Returns:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Calculates and sets the position of the square
        args:
            value (tuple): the position of the square
        """
        self.__position = value

    @property
    def size(self):
        """
        Get the size of the square
        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        args:
            value (int): the size value to be set
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Print a visual representation of the square.

        If the size is 0, it prints an empty line. Otherwise,
        it prints a square made of '#' characters,
        positioned according to the specified position.

        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()
