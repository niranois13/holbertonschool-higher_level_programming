#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while x > 0:
            print("{}".format(my_list[i]), end="")
            i += 1
            x -= 1
        print()
        return i
    except:
        print()
        return i
