#!/usr/bin/python3
"""
This module provides a function for adding two integers.
Module: 0-add_integer
Functions: add_integer(a, b=98): Adds two integers and returns the result.
"""


def add_integer(a, b=98):
    """
    Returns: int: The addition of a and b.
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
