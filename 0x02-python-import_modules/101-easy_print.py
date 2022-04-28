#!/usr/bin/python3
import os
if __name__ == "__main__":
    s = "#pythoniscool\n"
    line = str.encode(s)
    os.write(1, line)
