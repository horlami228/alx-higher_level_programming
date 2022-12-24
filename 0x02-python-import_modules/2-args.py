#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))

    else:
        print("{} arguments:".format(len(sys.argv)-1))

    n = len(sys.argv)-1

    for string in range(n):
        print("{}: {}".format(string, sys.argv[string + 1]))
