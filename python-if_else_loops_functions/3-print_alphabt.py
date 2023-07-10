#!/usr/bin/python3
# 3-print_alphabt.py

"""
Printing the ASCII alphabet in lowercase, excluding 'q' and 'e', not followed by a new line.
"""

output = ""
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        output += "{}".format(chr(letter))

print(output, end='')  # Print the output without a new line
