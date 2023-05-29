#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    re = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            re = re + 1
        except (ValueError, TypeError):
            pass
        print("")
        return (re)
