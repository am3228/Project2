from src.Statistics.Statistics import Mean
from src.Calculator.Square import square
from src.Calculator.Division import division

def Variance(data):
    try:
        meanData = Mean(data)
        totalVals = len(data)
        var = 0
        for a in data:
            var = var + square(a = meanData)
        result = division(var, totalVals)

        return result
    except ValueError:
        print("Error: That is an empty array. Please try again")