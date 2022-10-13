#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count is not x:
            print(my_list[count], end='')
            count++
    except:
        None
    print()
    return (count)

