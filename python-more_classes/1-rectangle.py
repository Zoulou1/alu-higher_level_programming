#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes.

The Rectangle class allows for the instantiation of objects representing a rectangle,
with optional width and height parameters, and includes property setters that enforce
type and value constraints.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0)
    height : int
        The height of the rectangle (default is 0)

    Methods
    -------
    width(self):
        Gets the width of the rectangle.
    width(self, value):
        Sets the width of the rectangle, ensuring it is a non-negative integer.
    height(self):
        Gets the height of the rectangle.
    height(self, value):
        Sets the height of the rectangle, ensuring it is a non-negative integer.
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, ensuring it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

