#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    operator = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    if sys.argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        calculator = operator[sys.argv[2]]
        first_operand = int(sys.argv[1])
        second_operand = int(sys.argv[3])

        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3],
                                     calculator(
            first_operand, second_operand)))
