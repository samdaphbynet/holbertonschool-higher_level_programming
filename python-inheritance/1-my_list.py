#!/usr/bin/python3
"""
class MyList that inherits from list
"""
class MyList(list):
    """
    A custom list class.

    Public instance method:
    - print_sorted(self): Prints the list in sorted order (ascending sort).
    """
    
    def print_sorted(self):
        """
        Print the list in sorted order.
        """
        sort = sorted(self)
        print(sort)
