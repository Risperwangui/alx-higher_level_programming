#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_list = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            multiple_list[count] = True
        else:
            multiple_list[count] = False
    return(multiple_list)
