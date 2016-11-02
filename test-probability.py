import probability
import unittest

class TestStatistics(unittest.TestCase):
    def test_uniform_pdf(self):

        self.assertEqual(probability.uniform_pdf(0.5), 1)

    def test_uniform_cdf(self):
        self.assertEqual(probability.uniform_cdf(0.5), 0.5)
        self.assertEqual(probability.uniform_cdf(2), 1)
        self.assertEqual(probability.uniform_cdf(-0.5), 0)

    def test_normal_pdf(self):

        result = round(probability.normal_pdf(0), 2)
        self.assertEqual(result, 0.4)

    def test_normal_cdf(self):

        self.assertEqual(probability.normal_cdf(-99999), 0.0)
        self.assertEqual(probability.normal_cdf(99999), 1.0)
        self.assertEqual(probability.normal_cdf(0), 0.5)


if __name__ == "__main__": unittest.main()
