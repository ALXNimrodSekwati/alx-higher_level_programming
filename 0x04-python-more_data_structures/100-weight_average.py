#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    decimal = 0

    for top in my_list:
        number += top[0] * top[1]
        decimal += top[1]

    return (number / decimal)
