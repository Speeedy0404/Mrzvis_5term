import matplotlib.image as mpimg
import numpy as np
from matplotlib import pyplot as plt

import Calculations
import Const
import WorkWithFile


def get_image_rgb():
    image = mpimg.imread(Const.image)
    image = (2.0 * image / 1.0) - 1.0
    return image


def vector_neurons():
    if Const.block_row == Const.block_max_row + 1 and Const.block_col != Const.block_max_col:
        Const.block_col += 1
        Const.block_row = 1
    elif Const.block_row == Const.block_max_row + 1 and Const.block_col == Const.block_col:
        Const.block_col = 1
        Const.block_row = 1

    vector = []
    size_1_1 = (Const.block_col - 1) * Const.block_width
    size_1_2 = Const.block_col * Const.block_width
    size_2_1 = (Const.block_row - 1) * Const.block_height
    size_2_2 = Const.block_row * Const.block_height
    for q in range(size_2_1, size_2_2):
        for y in range(size_1_1, size_1_2):
            for k in range(3):
                vector.append(array_image[q][y][k])

    return vector


def vector_neurons_for_saved_image():
    if Const.block_row == Const.block_max_row + 1 and Const.block_col != Const.block_max_col:
        Const.block_col += 1
        Const.block_row = 1
    elif Const.block_row == Const.block_max_row + 1 and Const.block_col == Const.block_col:
        Const.block_col = 1
        Const.block_row = 1

    vector = []
    size_1_1 = (Const.block_col - 1) * Const.compressed_block_width
    size_1_2 = Const.block_col * Const.compressed_block_width
    size_2_1 = (Const.block_row - 1) * Const.compressed_block_height
    size_2_2 = Const.block_row * Const.compressed_block_height
    for q in range(size_2_1, size_2_2):
        for y in range(size_1_1, size_1_2):
            for k in range(3):
                vector.append(Const.middle_image[q][y][k])

    return vector


def forward_propagation(vector, w):
    f_p = Calculations.multiplying_matrix_by_vector(vector, w)
    return f_p


def backward(x):
    Const.h1 = forward_propagation(x, Const.W1)
    Const.h2 = forward_propagation(Const.h1, Const.W2)

    delta_h2 = Calculations.subtracting_vectors(Const.h2, x)
    delta_h1 = Calculations.multiplying_matrix_transpose_by_vector(delta_h2, Const.W2)

    dw2 = Calculations.multiplying_matrix_by_alpha(
        Calculations.multiplying_matrix_by_transpose_matrix(delta_h2, Const.h1))

    dw1 = Calculations.multiplying_matrix_by_alpha(
        Calculations.multiplying_matrix_by_transpose_matrix(delta_h1, x))

    Const.W2 = Calculations.subtracting_two_matrices(Const.W2, dw2)
    Const.W1 = Calculations.subtracting_two_matrices(Const.W1, dw1)

    Const.W2 = Calculations.normalize(Const.W2)
    Const.W1 = Calculations.normalize(Const.W1)


def original_image():
    size_1 = 256
    size_2 = 256
    out_image = [[[0 for k in range(3)] for n in range(size_1)] for j in range(size_2)]

    for x in range(0, size_2):
        for y in range(0, size_1):
            for k in range(3):
                out_image[x][y][k] = array_image[x][y][k]

    return np.array(out_image)


def out_image(neurons):
    size_1_1 = (Const.block_col - 1) * Const.block_width
    size_1_2 = Const.block_col * Const.block_width
    size_2_1 = (Const.block_row - 1) * Const.block_height
    size_2_2 = Const.block_row * Const.block_height
    resize_out = -1

    for q in range(size_2_1, size_2_2):
        for y in range(size_1_1, size_1_2):
            for k in range(3):
                resize_out += 1
                Const.out_image[q][y][k] = neurons[resize_out]


def middle_image(neurons):
    size_1_1 = (Const.block_col - 1) * Const.compressed_block_width
    size_1_2 = Const.block_col * Const.compressed_block_width
    size_2_1 = (Const.block_row - 1) * Const.compressed_block_height
    size_2_2 = Const.block_row * Const.compressed_block_height
    resize_middle = -1
    for q in range(size_2_1, size_2_2):
        for y in range(size_1_1, size_1_2):
            for k in range(3):
                resize_middle += 1
                Const.middle_image[q][y][k] = neurons[resize_middle]

    Const.block_row += 1


def show(array):
    read_image = 1 * (np.array(array) + 1) / 2
    plt.axis('off')
    plt.imshow(read_image)
    plt.show()


def first_neural_network():
    if Const.get_number_blocks():
        pass
    else:
        print("Error: original image is not divided into blocks size " + str(Const.block_height) + "x" + str(
            Const.block_width) + ". Try blocks size: 1x1, 1x2, 2x1, 2x2, 4x4, 8x8, 8x4, 8x2 and other")
        exit()

    Const.W1, Const.W2 = Calculations.matrix_w(Const.first_layer, Const.second_layer)

    current_error = Const.ERROR + 1

    while current_error > Const.ERROR:
        Const.epoch += 1
        current_error = 0

        for y in range(Const.number_blocks):
            x = vector_neurons()
            backward(x)
            Const.block_row += 1

        for y in range(Const.number_blocks):
            x = vector_neurons()
            Const.h1 = forward_propagation(x, Const.W1)
            Const.h2 = forward_propagation(Const.h1, Const.W2)
            delta_h2 = Calculations.subtracting_vectors(Const.h2, x)
            current_error += Calculations.error_calculation(delta_h2, delta_h2)
            Const.block_row += 1

        print('Epoch : ', Const.epoch, '   ', 'errors : ', current_error, '   ', 'max errors : ', Const.ERROR)

    for y in range(Const.number_blocks):
        x = vector_neurons()

        Const.h1 = forward_propagation(x, Const.W1)
        Const.h2 = forward_propagation(Const.h1, Const.W2)

        out_image(Const.h2)
        middle_image(Const.h1)

    WorkWithFile.save_weight(Const.W1, "W1")
    WorkWithFile.save_weight(Const.W2, "W2")
    WorkWithFile.save_middle_image()

    h3 = original_image()
    show(h3)
    show(Const.middle_image)
    show(Const.out_image)

    number = Const.second_layer + 2
    number = number * (Const.first_layer + Const.number_blocks)
    number = (Const.first_layer * Const.number_blocks) / number
    print('Z = ', number)
    print("Iterations: ", Const.epoch / Const.number_blocks)


def second_neural_network():
    if Const.get_number_blocks():
        pass
    else:
        print("Error: original image is not divided into blocks size " + str(Const.block_height) + "x" + str(
            Const.block_width) + ". Try blocks size: 1x1, 1x2, 2x1, 2x2, 4x4, 8x8, 8x4, 8x2 and other")
        exit()

    Const.W1 = WorkWithFile.read_weight("W1")
    Const.W2 = WorkWithFile.read_weight("W2")

    for y in range(Const.number_blocks):
        x = vector_neurons()

        Const.h1 = forward_propagation(x, Const.W1)
        Const.h2 = forward_propagation(Const.h1, Const.W2)

        out_image(Const.h2)
        middle_image(Const.h1)

    h3 = original_image()
    show(h3)
    show(Const.middle_image)
    show(Const.out_image)

    number = Const.second_layer + 2
    number = number * (Const.first_layer + Const.number_blocks)
    number = (Const.first_layer * Const.number_blocks) / number
    print('Z = ', number)
    print("Iterations: ", Const.epoch / Const.number_blocks)


def third_neural_network():
    if Const.get_number_blocks():
        pass
    else:
        print("Error: original image is not divided into blocks size " + str(Const.block_height) + "x" + str(
            Const.block_width) + ". Try blocks size: 1x1, 1x2, 2x1, 2x2, 4x4, 8x8, 8x4, 8x2 and other")
        exit()

    Const.W2 = WorkWithFile.read_weight("W2")
    WorkWithFile.read_middle_image()

    for y in range(Const.number_blocks):
        x = vector_neurons_for_saved_image()

        Const.h2 = forward_propagation(x, Const.W2)

        out_image(Const.h2)
        Const.block_row += 1

    h3 = original_image()
    show(h3)
    show(Const.middle_image)
    show(Const.out_image)

    number = Const.second_layer + 2
    number = number * (Const.first_layer + Const.number_blocks)
    number = (Const.first_layer * Const.number_blocks) / number
    print('Z = ', number)


def main():
    value = True

    while value:
        print("№1 Обычная нейронка")
        print("№2 На обученных весах")
        print("№3 Из сжатой в разжатую")
        user_input = int(input("Выберите развитие 1-3: "))

        if user_input == 1:
            value = False
            first_neural_network()
        elif user_input == 2:
            value = False
            second_neural_network()
        elif user_input == 3:
            value = False
            third_neural_network()
        else:
            pass


array_image = get_image_rgb()
main()
