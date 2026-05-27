#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
