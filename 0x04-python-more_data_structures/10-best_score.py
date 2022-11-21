#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        key_list = list(a_dictionary.keys())
        value_list = list(a_dictionary.values())
    return (key_list[value_list.index(max(vale_list)]))
