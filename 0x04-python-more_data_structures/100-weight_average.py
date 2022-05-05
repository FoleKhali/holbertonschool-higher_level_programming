#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        a = []
        b = []
        for i in my_list:
            a += [i[0] * i[1]]
        for j in my_list:
            b += [j[1]]
        result = sum(a) / sum(b)
        return result
    return 0
