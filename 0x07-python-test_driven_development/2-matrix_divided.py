#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    This function divides the list in a matrix by the (div) argument

    :param matrix: Matrix
    :param div: Division element
    :return: Returns a new matrix with each list element divided
                and rounded to 2 decimal place
    """

    outer = []  # outer list
    inner = []  # inner list
    length = len(matrix[0])

    if not isinstance(div, (int, float)):  # check that div is a number
        raise TypeError("div must be a number")

    if div == 0:  # check that div is not 0
        raise ZeroDivisionError("division by zero")

    for layer in matrix:
        if len(layer) != length:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for element in layer:
                if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix "
                                    "(list of lists) of integers/floats")
                else:
                    inner.append(round((element / div), 2))
                    # append each element to an inner list
                    # rounded to 2 decimal places
            outer.append(inner)     # outside the loop append
            # the whole list to the outer list
            inner = []  # set the list to be empty before the next iteration

    return outer
