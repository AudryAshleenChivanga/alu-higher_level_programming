#!/usr/bin/python3
# 2-print_alphabet.py

"""Printing the ASCII alphabet in lower case , not followed by a new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
