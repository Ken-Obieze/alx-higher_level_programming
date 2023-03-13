#!/usr/bin/python3
"""Module to  writes a string to a UTF8 text file."""


def write_file(filename="", text=""):
    """
    write file method
    """
    with open(filename, 'w') as f:
        return f.write(text)
