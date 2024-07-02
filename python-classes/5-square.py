#!/usr/bin/python3
"""
Module 5-square

Defines a Square class with private size attribute and methods to compute area and print the square.
"""

class Square:
    """
    Represents a square.
    
    Attributes:
        __size (int): Private instance attribute representing the size of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a square object.
        
        Args:
            size (int): Optional. The size of the square. Defaults to 0.
        """
        self.size = size
    
    @property
    def size(self):
        """
        Getter method for size attribute.
        
        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.
        
        Args:
            value (int): The size value to set.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        """
        Computes the area of the square.
        
        Returns:
            int: The area of the square (size * size).
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
                print('#' * self.__size)

if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()
    
    print("--")
    
    my_square.size = 10
    my_square.my_print()
    
    print("--")
    
    my_square.size = 0
    my_square.my_print()
    
    print("--")
