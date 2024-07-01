#!/usr/bin/python3
"""
Module: 4-square

Defines a Square class with private size attribute,
area and my_print methods.
"""


class Square:
    """
    Square class defines a square by size and provides methods
    to calculate the area and print the square using '#'.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a specified size (default is 0).

        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.
        Raises TypeError if size is not an integer or ValueError if size is negative.

        Args:
            value (int): Size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: Area of the square (size^2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                line = '#' * self.__size
                print(line)
