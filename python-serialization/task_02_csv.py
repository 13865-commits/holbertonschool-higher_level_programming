#!/usr/bin/python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and saves it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to read.
    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # CSV sətirlərini lüğətlərdən ibarət siyahıya çeviririk
            data = [row for row in csv_reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
