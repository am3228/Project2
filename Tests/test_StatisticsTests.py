import unittest
import numpy as np
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import Csv_Reader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_results_property_statistics(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean(self):
        test_data = Csv_Reader('Tests/Data/Unit Test Mean.csv').data
        value_data = [int(row['Result']) for row in test_data]
        self.assertEqual(self.statistics.get_mean(value_data), 22.67)
        self.assertEqual(self.statistics.result, 22.67)

    def test_median(self):
        test_data = Csv_Reader('Tests/Data/Unit Test Median.csv').data
        value_data = [int(row['Result']) for row in test_data]
        self.assertEqual(self.statistics.get_median(value_data), 22)
        self.assertEqual(self.statistics.result, 22)

    def test_mode(self):
        test_data = Csv_Reader('Tests/Data/Unit Test Mode.csv').data
        value_data = [int(row['Result']) for row in test_data]
        self.assertEqual(self.statistics.get_mode(value_data), [32])
        self.assertEqual(self.statistics.result, [32])

    def test_variance(self):
        test_data = Csv_Reader('Tests/Data/Unit Test Variance.csv').data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.get_variance(value_data), np.var(value_data))
        self.assertEqual(self.statistics.result, np.var(value_data))

    def test_standard_deviation(self):
        test_data = Csv_Reader('Tests/Data/Unit Test Standard Deviation.csv').data
        value_data = [int(row['Value 1']) for row in test_data]
        self.assertEqual(self.statistics.get_standard_deviation(value_data), np.std(value_data), 3)
        self.assertEqual(self.statistics.result, np.std(value_data))

if __name__ == '__main__':
    unittest.main()