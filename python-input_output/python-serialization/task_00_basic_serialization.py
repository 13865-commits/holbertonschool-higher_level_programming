#!/usr/bin/python3
"""Module for basic serialization and deserialization of a dictionary."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file.

    Args:
        filename (str): The filename of the input JSON file.
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
