from Calculator.Addition import Addition
from Calculator.Division import Division
from Statistics.Statistics import Getsample


def Sample_Mean(data, sample_size):
    total = 0
    sample = Getsample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = Addition(total, num)
    return Division(total, num_values)
