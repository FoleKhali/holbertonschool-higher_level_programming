#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x:x**2, new_matrix)) for new_matrix in matrix]
