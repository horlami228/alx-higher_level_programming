#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv)-1))

    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))

    n = len(sys.argv)

    for string in range(1, n):
        print("{}: {}".format(string, sys.argv[string]))
