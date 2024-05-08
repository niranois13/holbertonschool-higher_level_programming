#!/usr/bin/python3
for f_digit in range(10):
    for l_digit in range(f_digit + 1, 10):
        if f_digit == 8 and l_digit == 9:
            print(f"{f_digit}{l_digit}".format(f_digit, l_digit))
        else:
            print(f"{f_digit}{l_digit}, ".format(f_digit, l_digit), end="")
