from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Getsample import Getsample


def Sample_Mean(data, sample_size):
    total = 0
    sample = Getsample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)
