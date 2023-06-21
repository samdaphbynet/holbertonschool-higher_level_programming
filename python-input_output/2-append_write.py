#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8) and
returns the number of characters added:
"""


def append_write(filename, text=""):
    """
    Ajoute ou écrit le texte spécifié dans un
    fichier existant ou crée un nouveau fichier.

    Args:
        filename (str): Le nom du fichier existant ou à créer.
        text (str, optionnel): Le texte à ajouter ou écrire dans le fichier.

    Returns:
        int: Le nombre de lignes ajoutées ou écrites dans le fichier.
    """
    with open(filename, "a" if filename else "w") as file:
        file.write(text)
        count = 0
        for line in text:
            count += 1
    return count
