#!/usr/bin/python3
"""check functions """


def inherits_from(obj, a_class):
    """check for object"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
