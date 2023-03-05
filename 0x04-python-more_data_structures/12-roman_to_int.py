#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'c': 100, 'D': 500, 'M': 1000}
    int_coversion = 0
    roman_list = list(roman_string)
    j = 0
    for i in roman_list:
        if i > 0:
            int_conversion += roman_dict[roman_list[j]] - 2 * roman_dict[roman_list[j - 1]]
        else:
            int_conversion = roman_dict[roman_list[j]]
        j += 1
    return(int_conversion)
