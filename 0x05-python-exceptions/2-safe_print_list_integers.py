#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x = 0):
    idx, count  = 0, 0
    while idx < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except (ValueError, TypeError):
            pass
        idx += 1
        print()
        return (count)
