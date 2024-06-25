#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())  # Sort keys alphabetically

    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
