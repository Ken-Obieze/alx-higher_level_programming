#!/usr/bin/python3
""" print_square module"""


def print_square(size):
    """
        prints square with character #.
        Args:
            size = size of square.
    """
    if isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
