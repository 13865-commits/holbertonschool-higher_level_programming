#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute.
"""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """
        Initialize the square.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.__size = size
