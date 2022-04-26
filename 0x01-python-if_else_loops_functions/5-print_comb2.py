#!/usr/bin/python3
for list_a in range(100):
    if list_a != 99:
        print("{:02d}".format(list_a), end=", ")
    elif list_a == 99:
        print("{}".format(list_a))
