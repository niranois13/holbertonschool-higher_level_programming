#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

discoveries = dir(hidden_4)

for secret in discoveries:
    if secret[:2] != "__":
        print("{}".format(secret))
