from Statistics.Mean import mean
from Calculator.Square import square
from Calculator.Division import division

def Variance(data):
    try:
        meanData = mean(data)
        totalVals = len(data)
        var = 0
        for a in data:
            var = var + square(a = meanData)
        result = division(var, totalVals)

        return result
    except ValueError:
        print("Error: That is an empty array. Please try again")