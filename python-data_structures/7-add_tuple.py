#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0] * 2

    for i in range(len(result)):
        if i < len(tuple_a):
            a = tuple_a[i]
        else:
            a = 0
        if i < len(tuple_b):
            b = tuple_b[i]
        else:
            b = 0
        result[i] = a + b

    return tuple(result)
