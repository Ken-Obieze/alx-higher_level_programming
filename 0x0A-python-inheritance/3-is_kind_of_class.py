#!/usr/bin/python3
"""Module for function to check if object is inatance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is an instance or inherited instance of a_class.
        False - if obj is not an instance or inherited instance of a class.
    """
    if isinstance(obj, a_class):
        return True
    return False
