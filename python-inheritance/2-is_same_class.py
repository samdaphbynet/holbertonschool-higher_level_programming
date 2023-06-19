#!/usr/bin/python3
# 2-is_same_class.py
# Zidani 6005@holbertonschool.com
"""
function that returns True if is instance ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance ; False otherwise.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
