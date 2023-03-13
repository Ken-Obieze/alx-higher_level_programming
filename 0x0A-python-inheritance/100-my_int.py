#!/usr/bin/python3
"""Module for implementation of a class MyInt that inherits from int."""


class myInt(int):
    """Defines class that inherits from int."""

    def __eq__(self, num):
        """Override equal and inverts it."""
        return int(self) != int(num)

    def __ne__(self, num):
        """Override not-equal and inverts it."""
        return int(self) == int(num)
