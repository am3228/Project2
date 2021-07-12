from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean
from Statistics.Standard_deviation import standard_deviation

def zscore(num):
    zmean = mean(num)
    sd = standard_deviation(num)
    zlist = []
    for z in num:
        z = round(((x - zmean) / sd), 6)
        zlist.append(z)
    return zlist
