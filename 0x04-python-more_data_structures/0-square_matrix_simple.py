#!/usr/bin/python3

#  computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    outer_list = []
    inner_list = []

    for inner in matrix:
        for num in inner:
            inner_list.append(num ** 2)
        outer_list.append(inner_list)
        inner_list = []
    return outer_list
