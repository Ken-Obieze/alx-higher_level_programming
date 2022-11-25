#!/usr/bin/python3
""" Defines square class"""


class Square:
    """ Square Module """
    def __init__(self, size=0):
        """ class initialisation

        Args:
            size: length of sides.

        Raises:
            TypeError: if size is not an int
            ValueError: if zize is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
