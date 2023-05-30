#!/usr/bin/python3
def print_last_digit(number):
    strn = repr(number)
    last = strn[-1]
    la = int(last)
    print("{}".format(la), end="")
    return la
