#!/usr/bin/python3
"""
This module provides a function to look up the attributes
and methods of a given object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
        
    Returns:
        list: A list of strings representing the object's attributes.
    """
    return dir(obj)
