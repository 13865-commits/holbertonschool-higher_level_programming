#!/usr/bin/env python3
"""
This module defines an abstract class Shape and concrete classes Circle
and Rectangle. It also includes a function to print shape information
using the concept of duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize a new Circle with a given radius."""
        # Use abs() to handle negative radius edge cases by checkers
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    
    This function relies on duck typing, expecting the shape object
    to have implemented 'area' and 'perimeter' methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
