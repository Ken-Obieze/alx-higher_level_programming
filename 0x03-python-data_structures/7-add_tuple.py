#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in  range(2):
        if tuple_a[i] < 0 or tuple_a[i] == ' ':
            tuple_a[i] = 0
        if tuple_b[i] < 0 or tuple_b[i] == ' ':
            tuple_b[i] = 0
        new_tuple[i] = tuple_a[i] + tuple_b[i]
    return (new_tuple)
