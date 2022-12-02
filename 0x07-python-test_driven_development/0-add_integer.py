#!/usr/bin/python3
""" Add integer module"""


def add_integer(a, b=98):
    """ 
        implements add_integer function
        Args:
            a: first number
            b: second number
        Returns:
            sum of two integers

    """

    if (type(a) not in [int, float] or a is None):
        raise TypeError("a must be an integer")
    if (type(b) not in [int, float] or b is None):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    return (a + b)
