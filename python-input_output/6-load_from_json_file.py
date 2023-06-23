#!/usr/bin/python3
"""
Ce script Python permet de charger des données à partir d'un fichier JSON.
"""
import json


def load_from_json_file(filename):
    """
    Charge les données à partir d'un fichier JSON.

    Args:
        filename (str): Le nom du fichier JSON à charger.

    Returns:
        dict: Les données chargées depuis le fichier JSON.
    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
