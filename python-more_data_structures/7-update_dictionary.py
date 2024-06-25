#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("Error: Dictionary is None.")
        return
    
    sorted_keys = sorted(a_dictionary.keys())  # Sort keys alphabetically
    
    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
