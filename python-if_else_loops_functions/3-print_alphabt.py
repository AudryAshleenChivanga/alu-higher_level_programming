#!/usr/bin/python3
# Printing all letters except for q and e
for letter in range(97, 123):
    if chr(letter) not in 'qe':
        print("{}".format(chr(letter)), end='')
