#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    else:
        big_key = list(a_dictionary.keys())[0]
        big_val = a_dictionary[big_key]
        for k, v in a_dictionary.items():
            if v > big_val:
                big_val = v
                big_key = k
    return (big_key)
