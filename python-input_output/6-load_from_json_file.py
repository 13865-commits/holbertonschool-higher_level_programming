#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'.

    Args:
        filename (str): The name of the JSON file to read.
    Returns:
        any: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
