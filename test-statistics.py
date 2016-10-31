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

    def test_mode(self):
        numbers = [20, 20, 20, 17, 17, 17, 15, 14, 13, 12, 11, 10]

        result = statistics.mode(numbers)
        expected_result = [17, 20]

        self.assertEqual(result, expected_result)

    def test_de_mean(self):
        numbers = [5,5,5,5,5]

        expected_result = [0.0, 0.0, 0.0, 0.0, 0.0]
        result = statistics.de_mean(numbers)

        self.assertEqual(result, expected_result)

    def test_variance(self):
        numbers = [3,4,6,5,7]

        expected_variance = 2.5
        variance = statistics.variance(numbers)

        self.assertEqual(variance, expected_variance)


    def test_standard_deviation(self):
        numbers = [5,4,6,5,7, 5,6]
        expected_deviation = 0.976

        deviation = statistics.standard_deviation(numbers)
        deviation = round(deviation, 3)

        self.assertEqual(deviation, expected_deviation)

    def test_interquartile_range(self):
        numbers = [6,6,6,6,6,6,6,1,1,5,5,5,6,5]
        expected_interquartile = 1

        interquartile = statistics.interquartile_range(numbers)

        self.assertEqual(interquartile, expected_interquartile)

if __name__ == "__main__": unittest.main()
