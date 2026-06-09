#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string.
    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
