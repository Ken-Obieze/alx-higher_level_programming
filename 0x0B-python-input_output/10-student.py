#!/usr/bin/python3
"""Module for class Student."""


class Student:
    """A defines a student."""

    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
            Args:
                first_name (str): name of student.
                last_name (str): name of student.
                age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieve dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """
        if attr is not None
            return {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
        else:
            return self.__dict__
