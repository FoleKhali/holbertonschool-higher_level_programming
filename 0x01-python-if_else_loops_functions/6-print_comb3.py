#!/usr/bin/python3
for list_a in range(0, 9):
    for list_b in range(1, 10):
        if list_b > list_a:
            if list_a != 8 or list_b != 9:
                print("{}{}" .format(list_a, list_b), end=", ")
            else:
                print("{}{}" .format(list_a, list_b))
