#!/usr/bin/python3
"""
This module defines a Square class for creating and managing squares with a 
position.
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to
            (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square ensuring it is an integer and not less 
        than 0.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square ensuring it is a tuple of 2 positive 
        integers.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # in stdout. Uses position for 
        offset.
        """
        if self.__size == 0:
            print()
            return
        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the print behavior of the Square instance.

        Returns:
            str: String representation of the square.
        """
        if self.__size == 0:
            return ""
        result = ["\n" * self.__position[1]]
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size + "\n")
        return "".join(result).rstrip()
