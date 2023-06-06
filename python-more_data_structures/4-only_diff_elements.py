#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    new1 = []
    for i in set_1:
        if i in set_2:
            continue
        else:
            new.append(i)
    for i in set_2:
        if i in set_1:
            continue
        else:
            new1.append(i)
    new.extend(new1)
    return new
