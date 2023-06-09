#!/usr/bin/python3

# Command line arguments

if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for num in range(1, n):
            print("{}: {}". format(num, sys.argv[num]))
