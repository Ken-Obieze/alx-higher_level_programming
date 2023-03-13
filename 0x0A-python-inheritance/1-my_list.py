#!/usr/bin/python3
"""Module implment MyList class that inherits from list."""


class MyList(list):
    """Implement a class that inherits from list."""

    def print_sorted(self):
        """Print list sorted in ascending order."""
        print(sorted(self))
