#!/usr/bin/python3
"""an square that has exceptions"""


class Square:
    """Square based on the 1.square.py that has exceptions"""
    def __init__(self, size=0):
        self.__size = size
        if (type(self.__size)) is not int:
            raise TypeError('size must be an integer')
        elif (self.__size < 0):
            raise ValueError('size must be >= 0')
