#!/usr/bin/python3
"""
Technical interview preparation:
"""


def pascal_triangle(n):
    """
    Génère un triangle de Pascal jusqu'à la rangée spécifiée.

    Args:
        n (int): Le nombre de rangées à générer dans le triangle de Pascal.

    Returns:
        list: Le triangle de Pascal représenté sous forme de liste de listes.
    """
    triangle = []
    for i in range(n):
        new_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                new_list.append(1)
            else:
                new_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(new_list)
    return triangle
