#!/usr/bin/python3
"""
This module defines a Rectangle class with properties for width and height,
as well as methods to calculate the area and perimeter of the rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle. If width or height is 0,
            returns 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using 'X'.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(['X' * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: The string representation of the rectangle object.
        """
        return f'<{self.__class__.__name__}({self.width}, {self.height})>'

# Testing the class
if __name__ == "__main__":
    # Test cases
    test_cases = [
        Rectangle(2, 4),
        Rectangle(2, 4),
        Rectangle(2, 4),
        Rectangle(0, 4),
        Rectangle(2, 0),
        Rectangle(0, 0)
    ]

    for index, rect in enumerate(test_cases):
        print(f"Case {index + 1}:")
        print(str(rect))
        print(repr(rect))
        print(rect)
        print("--")
