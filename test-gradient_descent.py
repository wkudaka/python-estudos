import gradient_descent as gd
import unittest
import random
import linear_algebra as lin_alg


class TestStatistics(unittest.TestCase):
    def test_sum_of_squares(self):
        numbers = [2,3,4]

        result = gd.sum_of_squares(numbers)
        self.assertEqual(result, 29)

    def test_difference_quotient(self):
        def square(x):
            return x**2
        #derivada da função acima...
        def square_derivative(x):
            return 2*x

        derivative_estimate = lambda x: gd.difference_quotient(square, x, h=0.00001)
        derivative_estimate_list = list(map(derivative_estimate, range(-5,5)))
        derivative_estimate_list = [round(item, 2) for item in derivative_estimate_list]

        square_derivative_list = list(map(square_derivative, range(-5,5)))

        #para um h pequeno, o resultado da derivada e da função
        #'difference_quotient' são basicamente os mesmos
        self.assertEqual(derivative_estimate_list, square_derivative_list)

    def test_step(self):
        def square(x):
            return x**2

        v = list(map(square, range(-3,4)))

        tolerance = 0.0000001

        while True:
            gradient = gd.sum_of_squares_gradient(v)
            next_v = gd.step(v, gradient, -0.01)
            if lin_alg.distance(next_v, v) < tolerance:
                break
            v = next_v

        rounded_v = [round(item, 2) for item in v]
        #quanto menor for a tolerância, mais perto v fica de zero
        self.assertEqual(rounded_v, [0.0,0.0,0.0,0.0,0.0,0.0,0.0])


if __name__ == "__main__": unittest.main()
