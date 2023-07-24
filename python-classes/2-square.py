#!/usr/bin/python3
"""Defining a square based on 1-square."""


class Square:
    """Representing the square."""


    def __init__(self, size=0):
        """Initializing a new square.
        Args:
            size (int): The size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
