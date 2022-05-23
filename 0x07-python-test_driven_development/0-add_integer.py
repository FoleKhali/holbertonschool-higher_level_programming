#!/usr/bin/python3
"""add two integers
you are not allowed to import modules"""


def add_integer(a, b=98):
    """return the addition of a and b raise type error
    if there is domething that it isn't a float or int"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a + b)
