#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        return (a_dictionary.pop(key))
    return (a_dictionary)