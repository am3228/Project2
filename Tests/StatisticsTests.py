import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from RandomGenerator.RandomIntegerList import random_integer_list
from numpy import var, std

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statsCalc = Statistics()
        self.allData = CsvReader('./pythonProject1/Tests/Unit_Test_Stats.csv').data
        self.testData = [int(row['Value']) for row in self.allData]
        self.testAnswers = CsvReader('./pythonProject1/Tests/Unit_Answers.csv').data
        self.list = random_integer_list(1, 10, 20, 50)

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statsCalc, Statistics)

    def test_mean(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mean(self.testData), float(row['Mean']))
            self.assertEqual(self.statsCalc.result, float(row['Mean']))

    def test_median(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.median(self.testData), float(row['Median']))
            self.assertEqual(self.statsCalc.result, float(row['Median']))

    def test_mode(self):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mode(self.testData), float(row['Mode']))
            self.assertEqual(self.statsCalc.result, float(row['Mode']))

    def test_variance_method(self):
        var_test_val = (var(self.testData))
        self.assertEqual(self.statsCalc.variance(self.testData), var_test_val)
        self.assertEqual(self.statsCalc.result, var_test_val)

    def test_standard_deviation(self):
        std_test_val = (std(self.testData))
        round_test = round(float(std_test_val), 8)
        self.assertAlmostEqual(self.statsCalc.standard_deviation(self.testData), round_test)
        self.assertAlmostEqual(self.statsCalc.result, round_test)