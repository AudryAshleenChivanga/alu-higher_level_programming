#!/usr/bin/python3

"""Defining a square based on the square 2."""


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
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
