from numpy.random import uniform

def Random_Decimal(start, end):
    rdec = uniform(start, end)
    round_dec = round(rdec, 2)
    return round_dec