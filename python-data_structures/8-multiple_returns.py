#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if sentence != "" else None
    tup = (length, first)
    return tuple(tup)
