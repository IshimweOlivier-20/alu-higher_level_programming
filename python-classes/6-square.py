#!/usr/bin/python3
"""
Module: 6-square

Defines a Square class with private size and position attributes,
area, and printing capabilities with specified positions.
"""


class Square:
    """
    Square class defines a square by size and position and provides methods
    to calculate the area and print the square using '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a specified size (default is 0) and position (default is (0, 0)).

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

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
        Setter method for setting the size of the square. Raises TypeError if size is not an integer or ValueError if size is negative.

        Args:
            value (int): Size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: Position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position of the square. Raises TypeError if position is not a tuple of 2 positive integers.

        Args:
            value (tuple): Position value to be set.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(v, int) for v in value) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

        Adjusts for the specified position where necessary.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
