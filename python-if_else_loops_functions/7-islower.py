#!/usr/bin/python3
# checks for lowercase character.


def islower(c):
    """Function is checking for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
