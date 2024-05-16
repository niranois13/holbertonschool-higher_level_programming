#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    result = 0
    x = 0
    while x < list_length:
        try:
            result = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)
        x += 1
    return result_list
