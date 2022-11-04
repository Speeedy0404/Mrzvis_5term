import random
from math import sqrt

import Const


# check
def matrix_w(one_layer, two_layer):
    w1 = [[0 for _ in range(two_layer)] for _ in range(one_layer)]
    w2 = [[0 for _ in range(len(w1))] for _ in range(len(w1[0]))]

    for row in range(one_layer):
        for col in range(two_layer):
            w1[row][col] = random.uniform(-1, 1)

    for col in range(len(w1)):  # col row
        for row in range(len(w1[0])):
            w2[row][col] = w1[col][row]

    return w1, w2


# check
def multiplying_matrix_by_vector(vector, w):
    size_1 = len(w)
    size_2 = len(w[0])
    neurons = []

    repetition = 0

    while repetition != size_2:

        variable = 0
        for element in range(size_1):
            variable += w[element][repetition] * vector[element]
            if element == size_1 - 1:
                neurons.append(variable)
        repetition += 1

    return neurons


# check
def subtracting_vectors(vector_one, vector_two):
    size = len(vector_one)
    vector_new = []

    for element in range(size):
        vector_new.append(vector_one[element] - vector_two[element])

    return vector_new


# check
def multiplying_matrix_by_transpose_matrix(matrix, matrix_transpose):
    size_1 = len(matrix_transpose)
    size_2 = len(matrix)

    matrix_new = [[0 for _ in range(size_2)] for _ in range(size_1)]

    for row in range(size_1):
        for col in range(size_2):
            matrix_new[row][col] = matrix_transpose[row] * matrix[col]

    return matrix_new


# check
def multiplying_matrix_by_alpha(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = matrix[row][col] * Const.alpha

    return matrix


# check
def subtracting_two_matrices(matrix_one, matrix_two):
    new_matrix = [[0 for _ in range(len(matrix_one[0]))] for _ in range(len(matrix_one))]

    for row in range(len(matrix_one)):
        for col in range(len(matrix_one[0])):
            new_matrix[row][col] = matrix_one[row][col] - matrix_two[row][col]

    return new_matrix


# check
def multiplying_matrix_transpose_by_vector(vector, matrix):
    new_matrix = []
    trans_result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            trans_result[row][col] = matrix[col][row]

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
