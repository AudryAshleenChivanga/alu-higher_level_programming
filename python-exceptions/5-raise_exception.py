#!/usr/bin/python3
def raise_exception():
    try:
        value = 1 / 'a'
    except TypeError:
        raise TypeError("Exception raised")
