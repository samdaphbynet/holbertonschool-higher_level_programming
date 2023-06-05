#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return 0
    elif idx >= len(my_list):
        return 0
    else:
        my_list[idx] = element
    return my_list
