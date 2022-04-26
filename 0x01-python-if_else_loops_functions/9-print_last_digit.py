#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10 if number > 10 else abs(number) % 10
    print(last, end='')
    return last
