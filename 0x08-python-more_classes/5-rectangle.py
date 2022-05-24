#!/usr/bin/python3
"""Contains the rectangle class"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Rectangle initializor"""
        self.width = width
        self.height = height

    def __del__(self):
        """delete the rectangle :c"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Width property function"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Height property function"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        """returns rec str"""
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for y in range(self.height - 1):
            string += '#' * self.width + '\n'
        string += '#' * self.width
        return string

    def __repr__(self):
        """Returns repr of the rec"""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return string

    def area(self):
        """area of a rectangle
        h*w = area"""
        return self.height * self.width

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2
