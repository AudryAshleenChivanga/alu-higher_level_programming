#!/usr/bin/python3
"""Defining  a square based on square number 2."""

class Square:
    """Representing a square."""


    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
