from Calculator.Division import Division
from Calculator.Subtraction import Subtraction
from Calculator.Addition import Addition

def Median(data):
    try:
        totalVals = len(data)
        list_numbers = [data[i] for i in range(totalVals)]
        list_numbers.sort()
        if totalVals % 2 == 0:
            median1 = list_numbers[int(totalVals // 2)]
            median2 = list_numbers[int(Subtraction((totalVals // 2), 1))]
            result = Division(Addition(median1, median2), 2)
        else:
            result = list_numbers[int(Division(totalVals, 2))]
        return result
    except ValueError:
        print("ERROR: That is an empty array! Please try again.")