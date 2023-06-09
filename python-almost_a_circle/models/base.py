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

    @staticmethod
    def from_json_string(json_string):
        """
        The function converts a JSON string to a Python object.
        Param json_string: A string containing JSON-formatted data
        Return: If the `json_string` parameter is `None` or an empty string,
        an empty list is returned.
        Otherwise, the method returns the result of parsing the `json_string`
        using the `json.loads()`
        method.
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This function creates an instance of a class
        (either Rectangle or Square) and updates its
        attributes using a dictionary.

        :param cls: The parameter `cls` refers to the
        class that the method is being called on. It is a
        convention to use `cls` instead of `self` when defining
        class methods
        :return: An instance of the class (either Rectangle,
        Square, or another class) with attributes
        updated based on the input dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        The function `load_from_file` loads data from a JSON file,
        creates instances of a class using the
        loaded data, and returns a list of the created instances.
        Param cls: The parameter `cls` is a reference to the class itself.
        It is used to access class
        attributes and methods within the class itself. In this case,
        it is used to dynamically generate
        the filename based on the class name
        Return: The method is returning a list of instances of the class.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                file_data = file.read()
        except FileNotFoundError:
            return []

        instance_data = cls.from_json_string(file_data)
        instances = []
        for data in instance_data:
            instance = cls.create(**data)
            instances.append(instance)
        return instances
