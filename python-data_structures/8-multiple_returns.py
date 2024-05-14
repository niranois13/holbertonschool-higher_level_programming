#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        length = len(sentence)
        first = sentence[0]
        tup = (length, first)
        return tuple(tup)
