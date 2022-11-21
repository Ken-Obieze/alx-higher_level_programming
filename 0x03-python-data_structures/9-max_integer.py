#!/usr/bin/python3
def max_integer(my_list=[]):
""" return biggest int in a list """
    maxVal = my_list[0]
    if len(my_list) == 0:
      	return None
    for i in my_list:
       	if i > maxVal:
        	max_val = i
        else:
        	continue
    return max_val
