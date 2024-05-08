#!/usr/bin/python3
for number in range(0, 99):
    if number // 10 == number % 10:
        continue
    elif number // 10 == number % 10 * 10 + number // 10:
        continue
    elif number == 89:
        print(f"{number:02d}")
    else:
        print(f"{number:02d}, ", end='')
