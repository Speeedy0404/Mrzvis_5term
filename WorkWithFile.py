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
    else:
        with open(file_name, 'w') as file:
            for a in range(len(weight)):
                for b in range(len(weight[0])):
                    file.write(str(weight[a][b]) + "\n")


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
        Const.compressed_block_width)+ '.txt'

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

    return matrix_weight
