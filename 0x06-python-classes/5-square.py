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
        self.__size = size

    @property
    def size(self):
        """ Gets current value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns area of tsquare """
        return (self.__size ** 2)
