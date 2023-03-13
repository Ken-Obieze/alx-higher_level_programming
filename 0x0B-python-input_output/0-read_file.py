#!/usr/bin/python3
""" function reads textfile """


def read_file(filename=""):
    """
    read a text file (UTF8) and prints to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
