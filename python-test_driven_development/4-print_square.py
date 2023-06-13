#!/usr/bin/python3
"""
This module prints a square of a given size.
Module: print_square
Function: print_square(size)
"""


def print_square(size):
    """
    print a square and check if size is an integer.
    """
    if size != int(size):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
