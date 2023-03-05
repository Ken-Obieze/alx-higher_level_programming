#!/usr/bin/python3
def weight_average(my_list=[]):
    mult = sum([x[0] * x[1] for x in my_list])
    summ = (sum([x[1] for x in my_list]) or 1)
    return mult / summ
