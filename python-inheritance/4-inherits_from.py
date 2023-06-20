#!/usr/bin/python3
# 4-inherits_from.py
"""
Function that returns True or False
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: An object to be checked.
        a_class: A class or type to compare against.

    Returns:
        True if the object is an instance of a class that inherited
        from the specified class,
        False otherwise.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
