#!/usr/bin/python3
"""defining write_file with two arguments"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return file.write(text)
