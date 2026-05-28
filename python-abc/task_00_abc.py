#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and its subclasses
Dog and Cat using the abc module.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the animal's sound."""
        pass


class Dog(Animal):
    """A Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """A Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
