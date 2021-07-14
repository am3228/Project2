from Statistics.Variance import variance
from Calculator.Squareroot import squareroot

def Standard_deviation(data):
    try:
        variance_data = variance(data)
        return squareroot(variance_data)

    except ValueError:
        print("ERROR: That is an empty array. Please try again.")