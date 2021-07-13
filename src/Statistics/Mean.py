from Calculator.Division import division

def mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)

    except ZeroDivisionError:
        print("Error: Cannot divide by 0")
    except ValueError:
        print("Error: Check your data inputs")