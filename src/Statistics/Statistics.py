from Calculator.Calculator import Calculator

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        a = len(self)
        b = float(sum(self))
        return b / a