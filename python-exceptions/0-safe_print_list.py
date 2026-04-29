#!/usr/bin/python3
"""Module that contains safe_print_list function"""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list and returns the real number printed"""
    nb_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_printed += 1
        except IndexError:
            break
    print("")
    return (nb_printed)
