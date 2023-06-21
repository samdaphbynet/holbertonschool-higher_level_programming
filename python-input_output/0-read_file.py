#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Reads the contents of a file specified by filename
    and prints it to stdout

    Args:
       filename (str): the name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
