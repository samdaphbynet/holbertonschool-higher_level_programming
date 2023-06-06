#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mx_value = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > mx_value:
            mx_value = my_list[i]
    return mx_value
