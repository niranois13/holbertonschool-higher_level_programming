#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argv = sys.argv[1:]

i = 0
result = 0
while i < len(argv):
    result += int(argv[i])
    i += 1

print("{}".format(result))
