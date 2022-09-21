#!/usr/bin/python3
def uppercase(str):
    upper = ''
    x = ord('a') - ord('A')
    for i in str:
        if ord(i) > 90:
            upper += chr(ord(i) - x)
        else:
            upper += i
        print("{:s}".format(upper))
