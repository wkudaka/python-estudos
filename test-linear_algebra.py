import linear_algebra as lin_alg
import math
import unittest


class TestLinearAlgebra(unittest.TestCase):
    def test_vector_add(self):
        v = [1, 2]
        w = [3,3]
        expected_result = [4, 5]

        result = lin_alg.vector_add(v, w)
        self.assertEqual(result, expected_result)

    def test_vector_subtract(self):
        v = [2, 2]
        w = [1, 1]
        expected_result = [1, 1]

        result = lin_alg.vector_subtract(v, w)
        self.assertEqual(result, expected_result)


    def test_vector_sum(self):
        v1 = [1.0,1.0]
        v2 = [1.0,1.0]
        v3 = [1.0,1.0]
        v4 = [1.0,1.0]
        vectors = [v1, v2, v3, v4]

        expected_result = [4, 4]

        result = lin_alg.vector_sum(vectors)
        self.assertEqual(result, expected_result)

    def test_scalar_multiply(self):
        num = 2
        vector = [1, 2, 3]
        expected_result = [2, 4, 6]

        result = lin_alg.scalar_multiply(num, vector)
        self.assertEqual(result, expected_result)

    def test_vector_mean(self):
        v = [2.0, 2.0]
        w = [4.0, 4.0]
        expected_result = [3.0, 3.0]
        vectors = [v,w]

        result = lin_alg.vector_mean(vectors)
        self.assertEqual(result, expected_result)

    def test_dot(self):
        v = [2, 2]
        w = [4, 4]
        expected_result = 16
        result = lin_alg.dot(v,w)

        self.assertEqual(result, expected_result)


    def test_sum_of_squares(self):
        v = [3, 3]
        expected_result = 18
        result = lin_alg.sum_of_squares(v)

        self.assertEqual(result, expected_result)

    def test_distance(self):
        v = [1,1]
        w = [1,2]
        expected_result = 1
        result = lin_alg.distance(v,w)

        self.assertEqual(result, expected_result)

    def test_make_matrix(self):

        result = lin_alg.make_matrix(5, 5, lin_alg.is_diagonal)
        expected_result = [
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,0,0,1]
        ]
        self.assertEqual(result, expected_result)

    def test_shape(self):
        matrix = [
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1]
        ]

        result = lin_alg.shape(matrix)
        expected_result = (3, 5)

        self.assertEqual(result, expected_result)

    def test_get_row(self):
        matrix = [
            [1,2,3],
            [4,5,6]
        ]

        result = lin_alg.get_row(matrix, 0)
        expected_result = [1, 2, 3]

        self.assertEqual(result, expected_result)

    def test_get_column(self):
        matrix = [
            [1,2,3],
            [4,5,6]
        ]

        result = lin_alg.get_column(matrix, 0)
        expected_result = [1, 4]

        self.assertEqual(result, expected_result)


if __name__ == "__main__": unittest.main()
