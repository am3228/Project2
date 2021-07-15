from Calculator.Division import Division

def Mean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return Division(total, num_values)

    except ZeroDivisionError:
        print("Error: Cannot divide by 0")
    except ValueError:
        print("Error: Check your data inputs")

#https://www.geeksforgeeks.org/numpy-mean-in-python/