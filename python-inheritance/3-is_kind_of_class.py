#!/usr/bin/python3
# file name: 3-is_kind_of_class.py
"""
function that returns True or False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or subclass of a specified class.

    Args:
        obj: An object to be checked.
        a_class: A class or type to compare against.

    Returns:
        True if the obj is an instance of the specified class, else False.
    """
    if isinstance(obj, a_class) or isinstance(obj, type(a_class())):
        return True
    else:
        return False
