#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1  # Get the number of command-line arguments

    if i == 0:
        print("{} arguments.".format(i))  # Print the number of arguments when there are none
    elif i == 1:
        print("{} argument:".format(i))  # Print the number of arguments when there is only one
    else:
        print("{} arguments:".format(i))  # Print the number of arguments when there are multiple

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))  # Print the index and value of each command-line argument
            i += 1
