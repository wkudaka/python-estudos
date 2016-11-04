import hypothesis_and_inference as hyp_inf
import unittest


class TestLinearAlgebra(unittest.TestCase):
    def test_normal_approximation_to_binomial(self):

        mu, sigma = hyp_inf.normal_approximation_to_binomial(1000, 0.5)

        self.assertEqual(mu, 500)
        self.assertEqual(round(sigma, 2), 15.81)


if __name__ == "__main__": unittest.main()
