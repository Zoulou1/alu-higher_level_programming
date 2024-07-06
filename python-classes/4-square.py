#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class represents a square with a private instance attribute size.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
