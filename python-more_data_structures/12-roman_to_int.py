#!/usr/bin/python3
def roman_to_int(roman_string):
    romain_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_value = 0
    for char in reversed(roman_string):
        value = romain_num[char]
        if value >= prev_value:
            num += value
        else:
            num -= value
        prev_value = value
    return num
