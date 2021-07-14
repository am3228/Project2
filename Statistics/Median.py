from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition

def median(data):
    try:
        totalVals = len(data)
        list_numbers = [data[i] for i in range(totalVals)]
        list_numbers.sort()
        if totalVals % 2 == 0:
            median1 = list_numbers[int(totalVals // 2)]
            median2 = list_numbers[int(subtraction((totalVals // 2), 1))]
            result = division(addition(median1, median2), 2)
        else:
            result = list_numbers[int(division(totalVals, 2))]
        return result
    except ValueError:
        print("ERROR: That is an empty array! Please try again.")

#
