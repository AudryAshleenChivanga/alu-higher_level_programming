#!/usr/bin/python3

# Check if the script is being run as the main module
if __name__ == "__main__":
    import sys

    # Calculate the number of command-line arguments
    i = len(sys.argv) - 1

    # Check the number of arguments and display appropriate message
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    # Print the index and value of each command-line argument
    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
