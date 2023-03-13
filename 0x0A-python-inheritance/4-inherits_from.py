#!/usr/bin/python3
"""Module to check if object inherits drectly or indirectly from class."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is an inherited instance of a_class
        False - If above condition fails.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
