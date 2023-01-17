#!/usr/bin/python3
"""Module for finding peak of a list."""


def find_peak(int_list):
    """Returns peak of a list."""

    if int_list == []:
        return None

    size = len(int_list)
    if size == 1:
        return int_list[0]
    else:
        return max(int_list)
    
    mid = int(size / 2)
    peak = int_list[mid]
    if peak > int_list[mid - 1] and peak > int_list[mid + 1]:
        return peak
    elif peak < int_list[mid - 1]:
        return find_peak(int_list[:mid])
    else:
        return find_peak(int_list[mid + 1:])
