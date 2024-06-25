#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_key = None
    highest_score = float('-inf')
    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            best_key = key

    return best_key
