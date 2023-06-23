#!/usr/bin/python3
"""
class Student that defines a student by:
    Public instance attributes
    Instantiation : first_name, last_name and age
    Public method : def to_json(self, attrs=None):
"""


class Student:
    """
    A class representing a Student.
    """
    def __init__(self, fisrt_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            fisrt_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = fisrt_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None, retrieve all attributes.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if attr in self.__dict__}
