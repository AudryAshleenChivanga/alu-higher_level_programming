#!/usr/bin/python3
import sys


def write():
    variable = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(variable + "\n")
    sys.exit(1)


write()
