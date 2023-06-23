#!/usr/bin/python3
"""
class Student that defines a student by:
    Public instance attributes
    Instantiation : first_name, last_name and age
    Public method : def to_json(self):
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

    def to_json(self):
        """
        Retrieve a disctionary representation of a Student instance.

        Returns:
            Dict: A dictionary representing the Student instance.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
