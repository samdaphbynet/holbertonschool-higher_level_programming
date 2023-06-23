#!/usr/bin/python3
"""
Function : that returns the dictionary
Description : with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    function that returns the dictionary
    """
    return obj.__dict__
