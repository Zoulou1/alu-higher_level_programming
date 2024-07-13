#!/usr/bin/python3
"""
This module defines a Square class for creating and managing squares.
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square ensuring it is a number and not less than 0.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares are equal based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares are not equal based on their area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if this square is less than another square based on their area.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if this square is less than or equal to another square based on 
        their area.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if this square is greater than another square based on their 
        area.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if this square is greater than or equal to another square based 
        on their area.
        """
        return self.area() >= other.area()
