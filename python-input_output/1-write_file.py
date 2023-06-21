#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Écrit le texte spécifié dans un fichier.

    Args:
        filename (str, optionnel): Le nom du fichier. Si aucun nom n'est fourni
        un fichier sans nom sera créé.
        text (str, optionnel): Le texte à écrire dans le fichier.

    Returns:
        int: Le nombre de lignes écrites dans le fichier.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        count = 0
        for line in text:
            count += 1
    return count
