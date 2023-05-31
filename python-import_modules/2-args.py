#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]

    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args != 1 else ''}:")

        for i, arg in enumerate(args):
            print(f"{i+1}: {arg}")
