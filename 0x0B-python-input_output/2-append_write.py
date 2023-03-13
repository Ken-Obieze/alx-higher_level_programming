#!/usr/bin/python3
"""Module for appending toa UTF8 file."""


def append_write(filename="", text=""):
    """
    method for appending string to file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
