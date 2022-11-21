#!/usr/bin/python3
def max_integer(my_list=[]):
    """ return biggest int in a list """
    if len(my_list) == 0:
        return (None)
    maxVal = my_list[0]
    for i in my_list:
        if i > maxVal:
            maxVal = i
        else:
            continue
    return (maxVal)
