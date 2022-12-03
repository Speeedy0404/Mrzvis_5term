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


#  Calculate weight matrix W:

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


def main():
    check = True
    while check:
        key = input("Взять стандартные set(1) или свои(2):\n")
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
        else:
            print('Некорретный ввод, повторите')


main()
