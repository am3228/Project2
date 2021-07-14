from collections import Counter

def Mode(data):
    try:
        totalVals = len(data)
        count = Counter(data)
        get_da_mode = dict(count)
        mode = [a for a, v in get_da_mode.items() if v == max(list(count.values()))]

        if len(mode) == totalVals:
            get_da_mode = "The mode was not found"
        else:
            get_da_mode = mode[0]

        return (get_da_mode)
    except ValueError:
        print("ERROR: That is an empty array. Please try again.")