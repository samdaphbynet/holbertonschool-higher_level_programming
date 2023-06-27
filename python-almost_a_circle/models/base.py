#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project.
The goal of it is to manage id attribute in all your future classes
and to avoid duplicating the same code (by extension, same bugs)
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        The function "to_json_string" returns a list of
        dictionaries as a JSON string, or an empty list if
        the input is None.

        Param list_dictionaries: A list of dictionaries
        that needs to be converted to a JSON string
        Return: If the input `list_dictionaries` is `None`,
        an empty list is returned. Otherwise, the input
        `list_dictionaries` is returned as is.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        The function "save_to_file" saves a list of objects
        to a file.
        Param list_objs: A list of objects that needs to be
        saved to a file.
        Return: None
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        to_dict = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(to_dict)
        with open(filename, "w") as f:
            f.write(json_string)
