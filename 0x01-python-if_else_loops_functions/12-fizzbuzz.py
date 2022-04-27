#!/usr/bin/python3
def fizzbuzz():
    for xd in range(1, 100):
        if (xd % 3 == 0 and xd % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (xd % 3 == 0 and xd % 5 != 0):
            print("Fizz", end=' ')
        elif (xd % 3 != 0 and xd % 5 == 0):
            print("Buzz", end=' ')
        else:
            print("{:d}".format(xd), end=' ')
    print("Buzz", end=' ')
