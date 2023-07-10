#!/usr/bin/python3

# Assuming uppercase() is defined in the "uppercase" module
from uppercase import uppercase

input_str = "best"
output_str = uppercase(input_str)
print("Input: '{}'".format(input_str))
print("Output: '{}'".format(output_str))

input_str = "Best School 98 Batter street"
output_str = uppercase(input_str)
print("Input: '{}'".format(input_str))
print("Output: '{}'".format(output_str))
