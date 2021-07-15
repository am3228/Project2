import statistics as stats

def standard_deviation(std_list):
    try:
        c = stats.standarddev(std_list)
        return c
    except (IndexError) or (ValueError):
        return none