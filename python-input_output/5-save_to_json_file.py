#!/usr/bin/python3
"""
save_to_json_file() function that writes an object to a test file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a test file, using json representation

    Args:
        my_obj (object): object to be written to file
        filename (str): name of file to be written to
    """
    with open(filename, "w") as outline:
        json.dump(my_obj, outline)
