import random
from math import sqrt

import Const


# check
def matrix_w(one_layer, two_layer):
    w1 = [[random.uniform(-1, 1) for _ in range(two_layer)] for _ in range(one_layer)]
    w2 = [[w1[row][col] for row in range(len(w1))] for col in range(len(w1[0]))]
    return w1, w2


# check
def multiplying_matrix_by_vector(vector, w):
    size = len(w[0])
    neurons = []
    repetition = 0
    while repetition != size:
        variable = 0
        for element in range(len(w)):
            variable += w[element][repetition] * vector[element]
            if element == len(w) - 1:
                neurons.append(variable)
        repetition += 1
    return neurons


# check
def subtracting_vectors(vector_one, vector_two):
    vector_new = []
    for element in range(len(vector_one)):
        vector_new.append(vector_one[element] - vector_two[element])
    return vector_new


# check
def multiplying_matrix_by_transpose_matrix(matrix, matrix_transpose):
    matrix_new = [[matrix_transpose[row] * matrix[col] for col in range(len(matrix))] for row in
                  range(len(matrix_transpose))]
    return matrix_new


# check
def multiplying_matrix_by_alpha(matrix):
    matrix = [[matrix[row][col] * Const.alpha for col in range(len(matrix[0]))] for row in
              range(len(matrix))]
    return matrix


# check
def subtracting_two_matrices(matrix_one, matrix_two):
    new_matrix = [[matrix_one[row][col] - matrix_two[row][col] for col in range(len(matrix_one[0]))] for row in
                  range(len(matrix_one))]
    return new_matrix


# check
def multiplying_matrix_transpose_by_vector(vector, matrix):
    new_matrix = []

    trans_result = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

    for col in range(len(trans_result[0])):
        value = 0
        for row in range(len(trans_result)):
            value += vector[row] * trans_result[row][col]
            if row == len(trans_result) - 1:
                new_matrix.append(value)

    return new_matrix


# check
def error_calculation(vector_one, vector_two):
    error = 0

    for element in range(len(vector_one)):
        error += vector_one[element] * vector_two[element]

    return error


# check
def normalize(matrix):
    for col in range(len(matrix[0])):
        value = 0

        for row in range(len(matrix)):
            value += matrix[row][col] * matrix[row][col]
        value = sqrt(value)

        for row in range(len(matrix)):
            matrix[row][col] = matrix[row][col] / value

    return matrix


# check
def get_number_blocks():
    if 256 % Const.block_height == 0 and 256 % Const.block_width == 0:
        return True
    else:
        return False


# check
def initialization():
    Const.out_image = [[[0 for _ in range(3)] for _ in range(256)] for _ in range(256)]
    Const.middle_image = [[[0 for _ in range(3)] for _ in range(Const.size1)] for _ in range(Const.size2)]
