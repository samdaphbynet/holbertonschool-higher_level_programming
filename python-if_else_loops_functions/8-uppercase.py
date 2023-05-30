#!/usr/bin/python3
def uppercase(str):
    upp = ""
    for i in str:
        char = chr(ord(i) - 32) if 97 <= ord(i) <= 122 else i
        upp += char
    print("{}".format(upp))
