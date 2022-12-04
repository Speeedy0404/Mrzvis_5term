import os

import numpy as np

import Const


# Take two sets of patterns:

def set_a_input_standard():
    x1 = np.array([1, 1, 1, 1, 1, 1]).reshape(6, 1)
    x2 = np.array([-1, -1, -1, -1, -1, -1]).reshape(6, 1)
    x3 = np.array([1, 1, -1, -1, 1, 1]).reshape(6, 1)
    x4 = np.array([-1, -1, 1, 1, -1, -1]).reshape(6, 1)

    Const.input_vectors = [x1, x2, x3, x4]


def set_b_target_standard():
    y1 = np.array([1, 1, 1]).reshape(3, 1)
    y2 = np.array([-1, -1, -1]).reshape(3, 1)
    y3 = np.array([1, -1, 1]).reshape(3, 1)
    y4 = np.array([-1, 1, -1]).reshape(3, 1)

    Const.out_vectors = [y1, y2, y3, y4]


def set_a_input_own():
    Const.input_vectors = []
    for i in range(4):
        x = []
        print('Входной set #', i)
        check = True
        while check:
            check = False
            entered_list = input("Введите список чисел , разделённых пробелом: ").split()
            if len(entered_list) != Const.set_input_size:
                check = True
                print("Неправильный размер входа, повторите")
            else:
                for number in range(Const.set_input_size):
                    x.append(int(entered_list[number]))
                x = np.array(x).reshape(Const.set_input_size, 1)
                Const.input_vectors.append(x)


def set_a_target_own():
    Const.out_vectors = []
    for i in range(4):
        y = []
        print('Выходной set #', i)
        check = True
        while check:
            check = False
            entered_list = input("Введите список чисел , разделённых пробелом: ").split()
            if len(entered_list) != Const.set_out_size:
                check = True
                print("Неправильный размер выхода, повторите")
            else:
                for number in range(Const.set_out_size):
                    y.append(int(entered_list[number]))
                y = np.array(y).reshape(Const.set_out_size, 1)
                Const.out_vectors.append(y)


def read_from_file(path, information, matrix=None):
    line_count = sum(1 for _ in open(path))

    if os.path.exists(path):
        with open(path, 'r') as file:
            for count in range(line_count):
                vector = []
                some_string = file.readline()
                for letter in some_string:

                    if letter == '-':
                        vector.append(-1)
                    elif letter == '#':
                        vector.append(1)
                    elif letter == "\n":
                        pass
                    else:
                        print('Неправильный формат шифрования')
                        exit()
                number = len(vector)
                vector = np.array(vector).reshape(number, 1)
                if information == 'input':
                    Const.input_vectors.append(vector)
                elif information == 'output':
                    Const.out_vectors.append(vector)
                elif information == 'noisy':
                    matrix.append(vector)
    else:
        print("Данные: " + path + " не хранятся")
        exit()

    if information == 'input':
        length = len(Const.input_vectors[0])
        for size in range(len(Const.input_vectors)):
            if len(Const.input_vectors[size]) != length:
                print('Ошибка: неодинаковая длина данных в', path)
                exit()
            else:
                pass
    elif information == 'output':
        length = len(Const.out_vectors[0])
        for size in range(len(Const.out_vectors)):
            if len(Const.out_vectors[size]) != length:
                print('Ошибка: неодинаковая длина данных в', path)
                exit()
            else:
                pass
    elif information == 'noisy':
        return matrix


def set_a_from_code():
    Const.input_vectors = []
    full_path = Const.path + Const.code[Const.number_of_code] + '_input.txt'
    read_from_file(full_path, 'input')
    pass


def set_b_from_code():
    Const.out_vectors = []
    full_path = Const.path + Const.code[Const.number_of_code] + '_output.txt'
    read_from_file(full_path, 'output')
    pass


# Calculate weight matrix W:

def calculate_weight_matrix_w():
    input_set = np.concatenate(
        (Const.input_vectors[0], Const.input_vectors[1], Const.input_vectors[2], Const.input_vectors[3]), axis=1)
    print('inputset')
    print(input_set)

    target_set = np.concatenate(
        (Const.out_vectors[0].T, Const.out_vectors[1].T, Const.out_vectors[2].T, Const.out_vectors[3].T), axis=0)
    print('targetset')
    print(target_set)

    print("\nWeight matrix:")
    Const.weight = np.dot(input_set, target_set)
    print(Const.weight)

    print("\n------------------------------")


def calculate_weight_matrix_w_for_code():
    input_set = None
    target_set = None
    size_one = len(Const.input_vectors)
    size_two = len(Const.out_vectors)

    for vector in range(1, size_one):
        if vector == 1:

            input_set = np.concatenate((Const.input_vectors[0], Const.input_vectors[vector]), axis=1)
        else:
            input_set = np.concatenate((input_set, Const.input_vectors[vector]), axis=1)

    print('inputset')
    print(input_set)

    for size in range(1, size_two):
        if size == 1:

            target_set = np.concatenate((Const.out_vectors[0], Const.out_vectors[size]), axis=1)
        else:
            target_set = np.concatenate((target_set, Const.out_vectors[size]), axis=1)
    target_set = target_set.T

    print('targetset')
    print(target_set)

    print("\nWeight matrix:")
    Const.weight = np.dot(input_set, target_set)
    print(Const.weight)

    print("\n------------------------------")


#  Test

def test_inputs(x, weight):
    # Multiply the input pattern with the weight matrix
    # (weight.T X x)
    y = np.dot(weight.T, x)
    y[y < 0] = -1
    y[y >= 0] = 1
    return np.array(y)


def test_targets(y, weight):
    # Multiply the target pattern with the weight matrix
    # (weight X y)
    x = np.dot(weight, y)
    x[x <= 0] = -1
    x[x > 0] = 1
    return np.array(x)


def testing_phase(input_vectors=None, out_vectors=None):
    check = True
    first = True

    out = []
    out_two = []
    inp = []
    inp_two = []

    if input_vectors is not None:
        # Test for Input Patterns: Set A
        print("\nTesting for input patterns: Set A")
        while check:
            check = False

            if first:
                out.clear()
                for element in range(len(input_vectors)):
                    out.append(test_inputs(input_vectors[element], Const.weight))
            else:
                out.clear()
                for element in range(len(inp_two)):
                    out.append(test_inputs(inp_two[element], Const.weight))

            inp.clear()
            for element in range(len(out)):
                inp.append(test_targets(out[element], Const.weight))

            out_two.clear()
            for element in range(len(inp)):
                out_two.append(test_inputs(inp[element], Const.weight))

            if first:
                for element in range(len(input_vectors)):
                    for size in range(len(input_vectors[element])):
                        if inp[element][size] != input_vectors[element][size]:
                            inp_two = inp
                            check = True
                            first = False
                            break
            else:
                for element in range(len(inp)):
                    for size in range(len(inp[element])):
                        if inp[element][size] != inp_two[element][size]:
                            inp_two = inp
                            check = True
                            break

            for element in range(len(out)):
                for size in range(len(out[element])):
                    if out[element][size] != out_two[element][size]:
                        check = True
                        break

            if check:
                pass
            else:
                for element in range(len(inp)):
                    print("\nOutput of input pattern" + str(element + 1))
                    print(test_inputs(inp[element], Const.weight))

    first = True
    check = True

    if out_vectors is not None:
        # Test for Target Patterns: Set B
        print("\nTesting for target patterns: Set B")
        while check:
            check = False

            if first:
                inp.clear()
                for element in range(len(out_vectors)):
                    inp.append(test_targets(out_vectors[element], Const.weight))

            else:
                inp.clear()
                for element in range(len(out_two)):
                    inp.append(test_targets(out_two[element], Const.weight))

            out.clear()
            for element in range(len(inp)):
                out.append(test_inputs(inp[element], Const.weight))

            inp_two.clear()
            for element in range(len(inp)):
                inp_two.append(test_targets(out[element], Const.weight))

            if first:
                for element in range(len(out_vectors)):
                    for size in range(len(out_vectors[element])):
                        if out[element][size] != out_vectors[element][size]:
                            out_two = out
                            check = True
                            first = False
                            break
            else:
                for element in range(len(out)):
                    for size in range(len(out[element])):
                        if out[element][size] != out_two[element][size]:
                            out_two = out
                            check = True
                            break

            for element in range(len(inp)):
                for size in range(len(inp[element])):
                    if inp[element][size] != inp_two[element][size]:
                        check = True
                        break

            if check:
                pass
            else:
                for element in range(len(out)):
                    print("\nOutput of input pattern" + str(element + 1))
                    print(test_targets(out[element], Const.weight))


# Test noisy

def to_try():
    variable = True
    while variable:
        print("\n")
        user_input = input("Проверить работоспособность сети при"
                           " распознавании эталонных образов? (yes), or any other letter for(no).\n")
        if user_input == "yes":
            x = []
            input_vector = []
            check = True
            while check:
                check = False
                print("Введите список чисел размером ", Const.set_input_size, " или ", Const.set_out_size,
                      ", разделённых пробелом:")
                entered_list = input().split()

                if len(entered_list) != Const.set_input_size:
                    if len(entered_list) != Const.set_out_size:
                        check = True
                elif len(entered_list) != Const.set_out_size:
                    if len(entered_list) != Const.set_input_size:
                        check = True

                if check:
                    print("Неправильный размер входа, повторите")
                else:
                    for number in range(len(entered_list)):
                        x.append(int(entered_list[number]))
                    x = np.array(x).reshape(len(entered_list), 1)
                    input_vector.append(x)
                if len(entered_list) == Const.set_input_size:
                    testing_phase(input_vector, None)
                elif len(entered_list) == Const.set_out_size:
                    testing_phase(None, input_vector)
        else:
            variable = False


def try_noisy_code():
    input_vectors = []
    full_path = Const.path + 'noisy_' + Const.code[Const.number_of_code] + '_input.txt'
    input_vectors = read_from_file(full_path, 'noisy', input_vectors)
    print('noisy_inputset')
    print(input_vectors)
    testing_phase(input_vectors, None)

    out_vectors = []
    full_path = Const.path + 'noisy_' + Const.code[Const.number_of_code] + '_output.txt'
    out_vectors = read_from_file(full_path, 'noisy', out_vectors)
    print('noisy_targetset')
    print(out_vectors)
    testing_phase(None, out_vectors)


def initialization():
    Const.set_input_size = (len(Const.input_vectors[0]))
    Const.set_out_size = (len(Const.out_vectors[0]))
    if len(Const.input_vectors) != len(Const.out_vectors):
        print('Ошибка: неодинаковое количество векторов входа и выхода')
        exit()


def main():
    check = True
    while check:
        key = input("Взять стандартные set(1) / свои(2) или взять зашифрованые символы(3):\n")
        if key == '1':
            check = False
            set_a_input_standard()
            set_b_target_standard()
            calculate_weight_matrix_w()
            testing_phase(Const.input_vectors, Const.out_vectors)
            to_try()
        elif key == '2':
            check = False

            check_two = True
            while check_two:
                check_two = False
                Const.set_input_size = int(input('Введите размер входного set 3<>15: \n'))
                Const.set_out_size = int(input('Введите размер выходного set 3<>15: \n'))
                if Const.set_input_size < 3 or Const.set_input_size > 15 or Const.set_out_size < 3 \
                        or Const.set_out_size > 15:
                    print('Некорретный ввод, повторите')
                    check_two = True

            set_a_input_own()
            set_a_target_own()
            calculate_weight_matrix_w()
            testing_phase(Const.input_vectors, Const.out_vectors)
            to_try()
        elif key == '3':
            check = False
            check_three = True

            while check_three:
                check_three = False

                print('Выберите входной set:\n'
                      '1) Танк')
                key_two = input()

                if key_two == '1':
                    Const.path = 'code/' + Const.code[0] + '/'
                    Const.number_of_code = 0
                else:
                    print('Некорретный ввод, повторите')
                    check_three = True
            set_a_from_code()
            set_b_from_code()
            initialization()
            calculate_weight_matrix_w_for_code()
            testing_phase(Const.input_vectors, Const.out_vectors)
            try_noisy_code()
        else:
            print('Некорретный ввод, повторите')


main()
