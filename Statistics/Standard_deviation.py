from Statistics.Variance import Variance
from Calculator.Squareroot import squareroot

def Standard_deviation(data):
    try:
        variance_data = Variance(data)
        return squareroot(variance_data)

    except ValueError:
        print("ERROR: That is an empty array. Please try again.")