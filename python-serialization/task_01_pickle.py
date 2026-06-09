#!/usr/bin/python3
"""Defines a custom object class with pickling capabilities."""
import pickle


class CustomObject:
    """Represents a custom object with serialization features."""

    def __init__(self, name, age, is_student):
        """Initializes the custom object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes in a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an instance from a file using pickle."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
