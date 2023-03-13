#!/usr/bin/python3
"""Module for definition of class Square based on 10-square.py."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string rerpresentation of instance."""
        return "[{}] {}/{}".format(type(self).__size, self.__size,
                                   self.__size)
