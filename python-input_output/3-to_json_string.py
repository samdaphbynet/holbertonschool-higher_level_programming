#!/usr/bin/python3
"""

"""
import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Args:
        my_obj (obj): L'objet Python à convertir en JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """
    return json.dumps(my_obj, sort_keys=True)
