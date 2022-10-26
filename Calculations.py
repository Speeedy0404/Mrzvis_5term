import random
from math import sqrt

import Const


# check
def matrix_w(one_layer, two_layer):
    w1 = [[0 for w in range(two_layer)] for y in range(one_layer)]

    for filling_line in range(one_layer):
        for filling_element in range(two_layer):
            w1[filling_line][filling_element] = random.uniform(-1, 1)

    w2 = [[0 for w in range(len(w1))] for y in range(len(w1[0]))]

    for a in range(len(w1)):#col row
        for b in range(len(w1[0])):
            w2[b][a] = w1[a][b]

    return w1, w2


# check
def multiplying_matrix_by_vector(vector, w):
    size_1 = len(w)
    size_2 = len(w[0])
    neurons = []

    repetition = 0

    while repetition != size_2:

        variable = 0
        for i in range(size_1):
            variable += w[i][repetition] * vector[i]
            if i == size_1 - 1:
                neurons.append(variable)
        repetition += 1
    return neurons


# check
def subtracting_vectors(vector_one, vector_two):
    size = len(vector_one)
    vector_new = []
    for i in range(size):
        vector_new.append(vector_one[i] - vector_two[i])

    return vector_new


# check
def multiplying_matrix_by_transpose_matrix(matrix, matrix_transpose):
    size_1 = len(matrix_transpose)
    size_2 = len(matrix)

    matrix_new = [[0 for w in range(size_2)] for y in range(size_1)]

    for i in range(size_1):
        for k in range(size_2):
            matrix_new[i][k] = matrix_transpose[i] * matrix[k]

    return matrix_new


# check
def multiplying_matrix_by_alpha(matrix):
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            matrix[i][k] = matrix[i][k] * Const.alpha

    return matrix


# check
def subtracting_two_matrices(matrix_one, matrix_two):
    new_matrix = [[0 for w in range(len(matrix_one[0]))] for y in range(len(matrix_one))]
    for i in range(len(matrix_one)):
        for k in range(len(matrix_one[0])):
            new_matrix[i][k] = matrix_one[i][k] - matrix_two[i][k]

    return new_matrix


# check
def multiplying_matrix_transpose_by_vector(vector, matrix):
    new_matrix = []
    transResult = [[0 for w in range(len(matrix))] for y in range(len(matrix[0]))]

    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            transResult[b][a] = matrix[a][b]

    for k in range(len(transResult[0])):
        value = 0
        for i in range(len(transResult)):
            value += vector[i] * transResult[i][k]
            if i == len(transResult) - 1:
                new_matrix.append(value)

    return new_matrix


def error_calculation(vector_one, vector_two):
    error = 0
    for i in range(len(vector_one)):
        error += vector_one[i] * vector_two[i]
    return error


def normalize(matrix):
    value = None
    for i in range(len(matrix[0])):
        value = 0
        for j in range(len(matrix)):
            value += matrix[j][i] * matrix[j][i]
        value = sqrt(value)
        for j in range(len(matrix)):
            matrix[j][i] = matrix[j][i] / value
    return matrix
