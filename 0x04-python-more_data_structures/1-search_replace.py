#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    j = 0
    for i in new_list:
        if i is search:
            new_list[j] = replace
        j++
    return (new_list)
