#!/usr/bin/python3
if __name__ == main:
    """function prints result of deveral arithmetic operations"""
    from calculator_1 import add, sub, mul, div 
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
