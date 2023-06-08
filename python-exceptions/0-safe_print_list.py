#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in my_list:
            print(i, end="")
            counter += 1
            if counter == x:
                break
        print()
        return counter
    except NameError:
        return counter
