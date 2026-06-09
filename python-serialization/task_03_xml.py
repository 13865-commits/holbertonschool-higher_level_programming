#!/usr/bin/python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data to.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserializes XML data from a file back into a dictionary.

    Args:
        filename (str): The filename of the XML file.
    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # XML elementlərini lüğətə (dictionary) çeviririk
        return {child.tag: child.text for child in root}
    except Exception:
        return None
