from Calculator.Calculator import Calculator
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.Standard_deviation import Standard_deviation
from Statistics.Variance import Variance
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.result = Mean(data)
        return self.result

    def median(self, data):
        self.result = Median(data)
        return self.result

    def Mode(self, data):
        self.result = Mode(data)
        return self.result

    def standard_deviation(self, data):
        self.result = Standard_deviation(data)
        return self.result

    def variance(self, data):
        self.result = Variance(data)
        return self.result

    pass