#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed_counts = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_counts += 1
        except (ValueError, TypeError):
            pass
        i += 1
        x -= 1
    print()
    return printed_counts
