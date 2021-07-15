from calculator.Calculator import Calculator
from .Mean import Mean
from .Median import Median
from .Mode import Mode
from .StandardDeviation import Standard_deviation
from .Variance import Variance

class Statistics(Calculator):

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

    def get_median(self, data):
        self.result = median(data)
        return self.result

    def get_mode(self, data):
        self.result = mode(data)
        return self.result

    def get_standard_deviation(self, data):
        self.result = standard_dev(data)
        return self.result

    def get_variance(self, data):
        self.result = variance(data)
        return self.result