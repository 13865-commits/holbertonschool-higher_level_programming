#!/usr/bin/env python3
"""
This module demonstrates the use of mixins in Python.
It defines SwimMixin, FlyMixin, and a Dragon class that uses them.
"""


class SwimMixin:
    """A mixin that provides swimming capabilities."""

    def swim(self):
        """Print a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying capabilities."""

    def fly(self):
        """Print a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits swimming and flying behaviors
    from mixins, and adds its own roaring behavior.
    """

    def roar(self):
        """Print a message indicating the dragon roars."""
        print("The dragon roars!")
