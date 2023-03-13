#!/usr/bin/python3
"""Module for checking if an object is instance of a class."""


def is_same_class(obj, a_class):
    """
    Check if object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is exactly an instance of a_class
        False - If obj is not an instant of a_class.
    """
    if type(obj) == a_class:
        return True
    return False
