#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'c': 100, 'D': 500, 'M': 1000}
    int_conversion = 0
    last_digit = 0
    roman_list = list(roman_string)
    for i in roman_list[::-1]:
        digit = roman_dict[i]
        if digit >= last_digit:
            int_conversion += digit
            last_digit = digit
        else:
            int_conversion -= digit
    return(int_conversion)
