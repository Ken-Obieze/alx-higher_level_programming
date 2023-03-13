#!/usr/bin/python3
"""Module define  a class MyInt that inherits from int."""


class myInt(int):
    """
        Invert int operator that inherits from int.
        Args:
            value (int): value to be compared
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        """Override equal and inverts it."""
        return not self.__eq__(value)

    def __ne__(self, value):
        """Override not-equal and inverts it."""
        return not self.__ne__(value)
