from Statistics.Statistics import Mean
from Calculator.Square import Square
from Calculator.Division import Division

def Variance(data):
    try:
        meanData = Mean(data)
        totalVals = len(data)
        var = 0
        for a in data:
            var = var + Square(a = meanData)
        result = Division(var, totalVals)

        return result
    except ValueError:
        print("Error: That is an empty array. Please try again")