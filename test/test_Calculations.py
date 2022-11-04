from unittest import TestCase

from Calculations import multiplying_matrix_by_vector, multiplying_matrix_by_transpose_matrix, \
    multiplying_matrix_transpose_by_vector


class Test(TestCase):

    def test_multiplying_matrix_by_vector(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8]
        ]
        vector = [1, 2, 3, 4]
        result = [50, 60]
        self.assertListEqual(result, multiplying_matrix_by_vector(vector, matrix))

    def test_multiplying_matrix_by_transpose_matrix(self):
        vector_one = [1, 2, 3, 4, 5, 6, 7]
        vector_two = [9, 8, 7, 6, 5]
        result = [
            [9, 18, 27, 36, 45, 54, 63],
            [8, 16, 24, 32, 40, 48, 56],
            [7, 14, 21, 28, 35, 42, 49],
            [6, 12, 18, 24, 30, 36, 42],
            [5, 10, 15, 20, 25, 30, 35]
        ]
        self.assertListEqual(result, multiplying_matrix_by_transpose_matrix(vector_one, vector_two))

    def test_multiplying_matrix_transpose_by_vector(self):
        vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        matrix = [
            [4, 2, 2, 4, 55, 86, 27, 78, 89],
            [11, 24, 37, 24, 55, 76, 97, 78, 69],
            [2, 4, 5, 2, 6, 3, 8, 1, 3],
            [21, 12, 43, 24, 35, 46, 71, 83, 93],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ]
        # transposed_matrix = [
        #     [4, 11, 2, 21, 1],
        #     [2, 24, 4, 12, 2],
        #     [2, 37, 5, 43, 3],
        #     [4, 24, 2, 24, 4],
        #     [55, 55, 6, 35, 5],
        #     [86, 76, 3, 46, 6],
        #     [27, 97, 8, 71, 7],
        #     [78, 78, 1, 83, 8],
        #     [89, 69, 3, 93, 9]
        # ]
        result = [2435, 2921, 172, 2719, 285]
        self.assertListEqual(result, multiplying_matrix_transpose_by_vector(vector, matrix))

