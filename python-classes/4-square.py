#!/usr/bin/python3

"""Defining a square based on square 3."""


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
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be greater than or equal to 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
