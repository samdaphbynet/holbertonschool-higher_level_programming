#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """
    Base class for objects with unique identifiers.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a base object.

        Args:
            id (int, optional): The identifier for the object.
                        If provided, it will be assigned to the id attribute.
                        If not provided, the id will be automatically generated
                        based on the __nb_objects count.
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
