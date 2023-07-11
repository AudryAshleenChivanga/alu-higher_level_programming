#!/usr/bin/python3
# Check if the script is being run as the main module
if __name__ == "__main__":
    import hidden_4

    # Iterate over the names in the imported module 'hidden_4'
    for name in dir(hidden_4):
        # Check if the name does not start with '__' (dunder) prefix
        if name[0] != '_' and name[1] != '_':
            # Print the name (module member) that satisfies the condition
            print(name)
