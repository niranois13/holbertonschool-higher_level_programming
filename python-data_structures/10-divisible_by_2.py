#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    i = len(new_list) - 1
    while i >= 0:
        if new_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
        i -= 1
    return new_list if new_list != [] else None
