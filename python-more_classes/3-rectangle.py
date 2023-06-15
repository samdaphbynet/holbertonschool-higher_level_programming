#!/usr/bin/python3
"""
class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    class Rectangle that defines a rectangle
    Attributes:
      length (int): length of the rectangle
      width (int): width of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle instance with optional width and height

        Args:
          width (int): width of the rectangle
          height (int): height of the rectangle
        """
        self.__height = 0
        self.__width = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width property
        Returns:
          int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width property

        Args:
          value (int): width of the rectangle
        Raises:
          TypeError: if value is not an int
          ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height property
        Returns:
          int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
          value (int): height of the value to set

        Raises:
          TypeError: if value is not an int
          ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns the area of the rectangle

        Returns:
          int: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle

        Returns:
          int: perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        Returns:
          str: string representation of the rectangle
        """
        rectangal = ""
        if self.width == 0 or self.height == 0:
            rectangal = ""
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rectangal += "#"
                if i < self.height - 1:
                    rectangal += "\n"
            return rectangal
