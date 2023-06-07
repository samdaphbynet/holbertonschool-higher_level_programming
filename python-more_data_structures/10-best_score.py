#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best = None
    b_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > b_value:
            best = key
            b_value = value
    return best
