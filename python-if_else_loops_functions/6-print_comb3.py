#!/usr/bin/python3
for number in range(0, 99):
    if number // 10 == number % 10:
        continue
    elif number // 10 == number % 10 * 10 + number // 10:
        continue
    else:
        print(f"{number:02d}")
