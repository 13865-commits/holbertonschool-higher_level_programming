#!/usr/bin/python3
"""
This module defines a Rectangle class with a class attribute
to count instances, along with private attributes, getters,
setters, area, perimeter, string representation, official
representation, and a destructor.
"""


class Rectangle:
    """A class that defines a rectangle."""

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for i in range(self.__height):
            rect_lines.append("#" * self.__width)

        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement instance counter upon deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
