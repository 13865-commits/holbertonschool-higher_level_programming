#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
