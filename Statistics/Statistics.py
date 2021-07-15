from Calculator.Calculator import Calculator
from .Mean import Mean
from .Median import Median
from .Mode import Mode
from .StandardDeviation import standard_deviation
from .Variance import Variance

class Statistics(Calculator):

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = Mean(data)
        return self.result

    def get_median(self, data):
        self.result = Median(data)
        return self.result

    def get_mode(self, data):
        self.result = Mode(data)
        return self.result

    def get_standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def get_variance(self, data):
        self.result = Variance(data)
        return self.result