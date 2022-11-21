#!/usr/bin/python3
def multiple_returns(sentence):
    """ Tuple with sting lenght is returned """
    stringTuple = ()
    if len(sentence) == 0:
        stringTuple = 0, "None"
    else:
        stringTuple = len(sentence), sentence[0]
    return stringTuple
