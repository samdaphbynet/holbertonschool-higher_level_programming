#!/usr/bin/python3
"""
class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.

    Args:
        Base (class): The base class providing
        a unique identifier for the rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's
                                position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's
                                position. Defaults to 0.
            id (int, optional): The identifier for the rectangle. If provided,
                                it will be assigned to the id attribute.
                                If not provided, the id will be automatically
                                generated based on the Base class.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Returns:
            None
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Returns:
            None
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            x (int): The x-coordinate of the rectangle's position.

        Returns:
            None
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            y (int): The y-coordinate of the rectangle's position.

        Returns:
            None
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        This function calculates the area of a rectangle
        using its width and height.

        Return: The function `area` is returning the product
                of the `width` and `height` attributes of the
                object.
        """
        return self.width * self.height

    def display(self):
        """
        This function displays a rectangle made of "#" characters
        with a height and width specified by
        the object's attributes.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        __str__ method so that it returns
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        widthHeight = f"{self.width}/{self.height}"
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {widthHeight}"

    def update(self, *args, **kwargs):
        """
        This function updates the attributes of an object either
        through positional arguments or keyword
        arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        This Python function returns a dictionary containing the
        id, width, height, x, and y attributes
        of an object.
        :return: A dictionary containing the attributes
        "id", "width", "height", "x", and "y" of an
        object.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
