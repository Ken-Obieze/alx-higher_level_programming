#!/usr/bin/python3

def add_integer(a, b = 98):
    if (type(a) != int or type(b) != int and 
            type(a) != float or type(b) != float):
        if (type(a) != int):
            raise TypeError(a must be an integer)
        if (type(b) != int):
            raise TypeError(b must be an integer)
    else:
        if (type(a) == float):
            a = int(a)
        if (type(b) == float):
            b = int(b)
        return (a + b)
