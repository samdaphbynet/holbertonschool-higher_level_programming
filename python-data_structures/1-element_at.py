#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    else:
        find = my_list.index(idx)
        find = my_list[idx]
    return find
