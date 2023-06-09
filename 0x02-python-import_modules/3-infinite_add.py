#!/usr/bin/python3

# This program adds arguments in the command line

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    else:
        sum = 0
        for num in range(1, len(sys.argv)):
            sum += int(sys.argv[num])
        print("{}".format(sum))
