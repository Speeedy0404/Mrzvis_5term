import os.path

import Const


def save_weight(weight, name):
    file_name = name + 'size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = "C:/PyCharm/МЗВИС/" + file_name

    if os.path.exists(file_path):
        print("Weights: " + file_name + " are already stored")
        print("Remove these files if you want to save new weight")
        # with open(file_name, 'w') as file:
        #     for a in range(len(weight)):
        #         for b in range(len(weight[0])):
        #             file.write(str(weight[a][b]) + "\n")
    else:
        with open(file_name, 'w') as file:
            for a in range(len(weight)):
                for b in range(len(weight[0])):
                    file.write(str(weight[a][b]) + "\n")


def save_middle_image():
    file_name = Const.name_image + 'size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = "C:/PyCharm/МЗВИС/" + file_name

    if os.path.exists(file_path):
        print("Image: " + file_name + " are already stored")
        print("Remove these files if you want to save new image")
    else:
        with open(file_name, 'w') as file:
            for a in range(len(Const.middle_image)):
                for b in range(len(Const.middle_image[0])):
                    for c in range(3):
                        file.write(str(Const.middle_image[a][b][c]) + "\n")


def read_weight(name):
    size_1 = 0
    size_2 = 0

    if name == "W1":
        size_1 = Const.first_layer
        size_2 = Const.second_layer
    elif name == "W2":
        size_1 = Const.second_layer
        size_2 = Const.first_layer
    matrix_weight = [[0 for w in range(size_2)] for y in range(size_1)]
    file_name = name + 'size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = "C:/PyCharm/МЗВИС/" + file_name

    if os.path.exists(file_path):
        with open(file_name, 'r') as file:
            for a in range(size_1):
                for y in range(size_2):
                    some_string = file.readline()
                    some_string.replace('\n', '')
                    matrix_weight[a][y] = float(some_string)
    else:
        print("Weights: " + file_name + " not stored")
        exit()

    return matrix_weight


def read_middle_image():
    file_name = Const.name_image + 'size_block' + str(Const.block_height) + 'x' + str(Const.block_width) + 'and' + str(
        Const.compressed_block_height) + 'x' + str(
        Const.compressed_block_width) + '.txt'

    file_path = "C:/PyCharm/МЗВИС/" + file_name

    if os.path.exists(file_path):
        with open(file_name, 'r') as file:
            for a in range(Const.size2):
                for b in range(Const.size1):
                    for c in range(3):
                        some_string = file.readline()
                        some_string.replace('\n', '')
                        Const.middle_image[a][b][c] = float(some_string)
    else:
        print("Image: " + file_name + " not stored")
        exit()
