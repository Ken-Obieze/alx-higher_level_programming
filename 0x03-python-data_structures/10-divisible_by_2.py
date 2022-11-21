#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ checks if numbers in list are even"""
    evenCheck = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            evenCheck.append(True)
        else:
            evenCheck.append(False)
        return evenCheck
