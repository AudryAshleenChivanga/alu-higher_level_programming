#!/usr/bin/python3

"""Defines a square based on Square 5."""

class Square:
    """Representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square.
        Args:
            size (int): The size of the new Square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        Raises:
            TypeError: If size is not an integer, or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0, or if position contains negative integers.
        """
        self.size = size
        self.position = position

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
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The new position of the square as a tuple of 2 positive integers.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position contains negative integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in value):
            raise ValueError("position must contain positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters.
        If size is equal to 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
