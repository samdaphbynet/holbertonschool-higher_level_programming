#!/usr/bin/python3
"""
This module provides a function to print a person's name.
Module: say_my_name
Function: prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Print a person's name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = "{} {}".format(first_name, last_name)
    else:
        full_name = first_name

    print("My name is {}".format(full_name))
