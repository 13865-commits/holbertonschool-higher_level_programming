#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute
and performs size validation.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initialize the square.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
