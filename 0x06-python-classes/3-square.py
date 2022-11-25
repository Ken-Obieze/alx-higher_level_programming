#!/usr/bin/python3
""" Defines Square"""


class Square:
    """ represents square """

    def __init__(self, size=0):
        """ initializes new square.

        Args:
            size: size of square

        Raises:
            TypeError: if type is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < o:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns area of tsquare """
        return (self.__size ** 2)
