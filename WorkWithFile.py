import os.path

import Const


def save_weight(weight, name):
    file_name = name + '_size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = os.path.join("saved_weights/", file_name)

    if os.path.exists(file_path):
        print("Weights: " + file_name + " are already stored")
        print("Do you want overwrite them")
        check = input(" Yes(Y) / No(N) : ")

        if check == "Y" or "y":
            with open(file_name, 'w') as file:
                for a in range(len(weight)):
                    for b in range(len(weight[0])):
                        file.write(str(weight[a][b]) + "\n")
            print("Overwrite has occurred successfully")
        else:
            pass

    else:
        with open(file_path, 'w') as file:
            for row in range(len(weight)):
                for col in range(len(weight[0])):
                    file.write(str(weight[row][col]) + "\n")


def save_middle_image():
    file_name = Const.name_image + '_size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = os.path.join("saved_compressed_images/", file_name)

    if os.path.exists(file_path):
        print("Image: " + file_name + " are already stored")
        print("Remove these files if you want to save new image")
    else:
        with open(file_path, 'w') as file:
            for row in range(len(Const.middle_image)):
                for col in range(len(Const.middle_image[0])):
                    for rgb in range(3):
                        file.write(str(Const.middle_image[row][col][rgb]) + "\n")


def read_weight(name):
    size_1 = 0
    size_2 = 0

    if name == "W1":
        size_1 = Const.first_layer
        size_2 = Const.second_layer
    elif name == "W2":
        size_1 = Const.second_layer
        size_2 = Const.first_layer

    matrix_weight = [[0 for _ in range(size_2)] for _ in range(size_1)]

    file_name = name + '_size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = os.path.join("saved_weights/", file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for row in range(size_1):
                for col in range(size_2):
                    some_string = file.readline()
                    some_string.replace('\n', '')
                    matrix_weight[row][col] = float(some_string)
    else:
        print("Weights: " + file_name + " not stored")
        exit()

    return matrix_weight


def read_middle_image():
    file_name = Const.name_image + '_size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = os.path.join("saved_compressed_images/", file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for row in range(Const.size2):
                for col in range(Const.size1):
                    for rgb in range(3):
                        some_string = file.readline()
                        some_string.replace('\n', '')
                        Const.middle_image[row][col][rgb] = float(some_string)
    else:
        print("Image: " + file_name + " not stored")
        exit()
