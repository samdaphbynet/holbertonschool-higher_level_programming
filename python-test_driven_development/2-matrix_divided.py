#!/usr/bin/python3
"""
this module is used to divide a matrix by a number
module: matrix_divided
Function: matrix_divided(matrix, div) divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Returns: matrix with all elements divided by a number
    """
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        result.append([round(num / div, 2) for num in row])
    return result
