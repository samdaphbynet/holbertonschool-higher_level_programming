#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            print("{}".format(num), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
