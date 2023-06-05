#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for i in my_string:
        if i == 'c':
            continue
        elif i == 'C':
            continue
        else:
            newString += i
    return newString
