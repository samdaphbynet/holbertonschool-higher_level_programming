#!/usr/bin/python3
"""
Function that return the list of available attributes and metthods of an object
"""


def lookup(obj):
    """
    Returns: the list of available attributes and metthods of an object
    """
    return dir(obj)
