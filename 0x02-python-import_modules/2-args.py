#!/usr/bin/python3
import sys
if __name__ == "__main__":
    a = len(sys.argv)
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        for i in range(1, a):
            print("{}: {}".format(a - 1, sys.argv[i]))
    else:
        print("{} arguments:" .format(a - 1))
        for i in range(1, a):
            print("{:d}: {}".format(i, sys.argv[i]))
