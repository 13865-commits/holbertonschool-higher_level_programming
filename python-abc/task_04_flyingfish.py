#!/usr/bin/env python3
"""
This module explores multiple inheritance by creating a FlyingFish
class that inherits from both Fish and Bird classes.
"""


class Fish:
    """A Fish class representing a water-dwelling creature."""

    def swim(self):
        """Print the swimming behavior of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A Bird class representing an airborne creature."""

    def fly(self):
        """Print the flying behavior of the bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A FlyingFish class inheriting from both Fish and Bird."""

    def fly(self):
        """Print the specific flying behavior of the flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the specific swimming behavior of the flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the specific habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
