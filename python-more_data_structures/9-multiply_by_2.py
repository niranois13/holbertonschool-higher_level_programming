#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = a_dictionary.copy()
    for k, v in a_dictionary_copy.items():
        a_dictionary_copy.update({k: v * 2})
    return a_dictionary_copy
