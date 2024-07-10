#!/usr/bin/python3
"""
This module provides a function to list all attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attributes and methods available for the object.
    """
    return dir(obj)
