#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list) - 1
    for i in my_list:
        if idx < 0:
            return None
        elif idx > a:
            return None
        else:
            return a
