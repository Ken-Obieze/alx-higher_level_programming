#!/usr/bin/python3
""" MagicClass Module"""


import math


class MagicClass:
    """ magicClass Definition"""

    def __init__(self, radius=0)
        """ initialises new MagicClass
        Args:
            radius: radius of MagicClass
        Raises:
            TypeError: when radius isn't int or float
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self)
        """ Retuen area of Magic Class"""
        return (math.pi * self.__radius ** 2)

    def circumference(self)
        """ Return circumference of magicClass"""
        return (2 * math.pi * self.__radius)
