from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Standard_deviation import standard_deviation
from Statistics.Variance import variance
from Statistics.ZScore import zscore
from Statistics.SampleMean import samplemean
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        a = len(self)
        b = float(sum(self))
        return b / a

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result