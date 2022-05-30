#!/usr/bin/python3
"""return true if its exactly an intance, otherwise, return false"""
def is_same_class(obj, a_class):
    """check if object is an instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
