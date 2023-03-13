#!/usr/bin/python3
"""Module define a class MyInt that inherits from int."""


class myInt(int):
    """Invert int operator that inherits from int."""

    def __eq__(self, value):
        """Override equal and inverts it."""
        return self.real != value

    def __ne__(self, value):
        """Override not-equal and inverts it."""
        return self.real == value
