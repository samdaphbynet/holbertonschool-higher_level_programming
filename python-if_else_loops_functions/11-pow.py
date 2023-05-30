#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b >= 0:
        for _ in range(b):
            p = p * a
    else:
        for _ in range(abs(b)):
            p = p / a
    return p
