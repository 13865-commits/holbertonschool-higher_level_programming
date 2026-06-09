#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.
    Returns:
        any: The Python object represented by my_str.
    """
    return json.loads(my_str)
