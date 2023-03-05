#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'c': 100, 'D': 500, 'M': 1000}
    int_coversion = 0
    roman_list = list(roman_string)
    for i, c  in enumerate(roman_list):
        if (i+1) == len(roman_string) or roman_dict[c] >= roman_dict[roman_list[i+1]]::
            int_conversion += roman_dict[c]
        else:
            int_conversion -= roman_dict[c]
    return(int_conversion)
