import statistics
import math
import unittest


class TestStatistics(unittest.TestCase):
    def test_mean(self):
        numbers = [5,5,5,5,5]

        expected_result = 5.0
        result = statistics.mean(numbers)

        self.assertEqual(result, expected_result)

    def test_median_with_odd_length(self):
        numbers = [1,2,3,4,5]

        expected_result = 3
        result = statistics.median(numbers)
        self.assertEqual(result, expected_result)


    def test_median_with_even_length(self):
        numbers = [1,2,3,4,5,6]

        expected_result = 3.5
        result = statistics.median(numbers)

        self.assertEqual(result, expected_result)

    def test_quantile(self):
        numbers = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

        self.assertEqual(statistics.quantile(numbers, 0.1), 11)
        self.assertEqual(statistics.quantile(numbers, 0.3), 13)
        self.assertEqual(statistics.quantile(numbers, 0.5), 15)
        self.assertEqual(statistics.quantile(numbers, 0.8), 18)


if __name__ == "__main__": unittest.main()
