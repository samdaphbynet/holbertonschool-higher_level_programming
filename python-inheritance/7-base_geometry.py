#!/usr/bin/python3
# NameFile: 7-base_geometry.py
"""
This file contains the difinition of the BaseGeometry class.
"""


class BaseGeometry:
    """
    The BaseGeometry class is a base class for geometry.
    """
    def area(self):
        """
        Abstract method to calculate the area.
        It raises an exception if not implemented in derived classes.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if the value is a positive integer
        and raises appropriate exception if not.
        Args:
            name (str): the name of the parameter to be validated.
            value (int): the value to be validated.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is negative.

        Returns:
            int: the validated value if it passes the validation.
        """
        name = str(name)
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
