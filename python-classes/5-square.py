#!/usr/bin/python3
"""
This module defines a Square class that represents a square and provides methods
to calculate its area and print it using '#' characters.
"""

class Square:
    """
    Square class represents a square.

    Attributes:
        __size (int): Private attribute to store the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square object with a given size.

        Args:
            size (int): Optional size of the square (default is 0).
                         Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

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

        Args:
            value (int): Size of the square. Must be a non-negative integer.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: Area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

# Example usage:
if __name__ == "__main__":
    s = Square(5)
    print(s.size)  # Output: 5
    print(s.area())  # Output: 25
    s.my_print()

