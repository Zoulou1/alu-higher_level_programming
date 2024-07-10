#!/usr/bin/python3
"""
This module provides a class MyList that inherits from the built-in list class
and includes a method to print the list in sorted order.
"""

class MyList(list):
    """
    A subclass of list that provides an additional method to print
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
