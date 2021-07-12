from Calculator.Calculator import Calculator
from Statistics.Mean import mean
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