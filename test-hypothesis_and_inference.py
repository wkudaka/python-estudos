import hypothesis_and_inference as hyp_inf
import unittest


class TestLinearAlgebra(unittest.TestCase):
    def test_normal_approximation_to_binomial(self):

        mu, sigma = hyp_inf.normal_approximation_to_binomial(1000, 0.5)

        self.assertEqual(mu, 500)
        self.assertEqual(round(sigma, 2), 15.81)

    def test_normal_two_sided_bounds(self):
        mu, sigma = hyp_inf.normal_approximation_to_binomial(1000, 0.5)
        lo, hi = hyp_inf.normal_two_sided_bounds(0.95, mu, sigma)

        self.assertEqual(round(lo, 2), 469.01)
        self.assertEqual(round(hi, 2), 530.99)

    def test_a_b_test_statistic(self):
        z = hyp_inf.a_b_test_statistic(1000, 200, 1000, 180)
        self.assertEqual(round(z, 2), -1.14)


if __name__ == "__main__": unittest.main()
