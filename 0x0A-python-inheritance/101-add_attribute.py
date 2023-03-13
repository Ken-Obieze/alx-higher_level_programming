#!/usr/bin/python3
"""Module defining pfunction to add atribute to object."""


def add_attribute(obj, name, value):
    """Implement method for adding new attributes."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
