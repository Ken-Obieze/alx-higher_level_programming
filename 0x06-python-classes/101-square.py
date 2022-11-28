#!/usr/bin/python3
""" Defines Square"""


class Square:
    """ represents square """

    def __init__(self, size=0, position=(0, 0)):
        """ initializes new square.

        Args:
            size: size of square
            position: position of square

        Raises:
            TypeError: if type is not an int
            ValueError: if value is less than 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Gets current value of size"""
        return (self.__size)

    @property
    def position(self):
        """ Gets position values"""
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ returns area of tsquare """
        return (self.__size ** 2)

    def my_print(self):
        """ prints square with character '#'"""
        if self.size == 0:
            print('')
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print('')

    def __str__(self):
        """ prints square with character '#'"""
        if self.size == 0:
            print('')
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print('')
