#!/usr/bin/python3
"""My File Square."""


class Square:
    """The square"""
    def __init__(self, size=0):
        self.__size = size
        if (type(self.__size)) is not int:
            raise TypeError('size must be an integer')
        elif (self.__size < 0):
            raise ValueError('size must be >= 0')

    def area(self):
        return(self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value)) is not int:
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
