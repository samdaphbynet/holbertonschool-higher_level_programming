#!/usr/bin/python3
"""
class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class is a subclass of Rectangle that initializes
    with equal height and width and has a
    string representation indicating it is a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property 
    def size(self):
        """
        This is a Python property method that returns the value of the "width" attribute as the "size".
        :return: The `size` property is returning the value of the `width` attribute of the object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter method in Python that sets the width and height of an object to a given integer
        value.
    
        param value: The value that is being set for the size attribute of an object
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """
        This function returns a string representation of a Square object, including its ID, coordinates,
        and height.
        :return: The `__str__` method is returning a string representation of a `Square` object. The
        string includes the object's `id`, `x` and `y` coordinates, and `height`. The format of the
        string is "[Square] (id) x/y - height".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
