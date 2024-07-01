#!/usr/bin/python3
"""
This module defines the Square class.

The Square class represents a square with a private instance attribute 'size'.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
