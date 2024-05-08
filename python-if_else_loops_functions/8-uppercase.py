#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        i = ord(c)
        if i >= 97 and i <= 122:
            i -= 32
        result += chr(i)
    print(result)
