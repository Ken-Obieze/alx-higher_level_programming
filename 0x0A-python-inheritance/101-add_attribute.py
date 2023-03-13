#!/usr/bin/python3
"""Module defining pfunction to add atribute to object."""


def add_attribute(obj, name, value):
    """Implement method for adding new attributes."""
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") \
            and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
