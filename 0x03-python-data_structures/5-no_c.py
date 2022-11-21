#!/usr/bin/python3
def no_c(my_string):
    """ function that removes c from strings """
    return (my_string.translate({ord(char): None for char in "cC"}))
