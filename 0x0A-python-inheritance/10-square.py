#!/usr/bin/python3
"""Module for definition of class Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.
        
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
