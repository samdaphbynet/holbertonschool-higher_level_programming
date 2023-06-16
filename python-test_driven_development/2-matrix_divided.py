#!/usr/bin/python3
"""
this module is used to divide a matrix by a number
module: matrix_divided
Function: matrix_divided(matrix, div) divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by a number
    :param matrix: a matrix
    :param div: a number
    :return: a matrix
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(error)
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or matrix == []:
        raise TypeError(error)
    new = []
    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        sub = []
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

            elif not isinstance(div, (int, float)):
                raise TypeError("div must be a number")

            sub.append(round(ele / div, 2))

        new.append(sub)

    return new
