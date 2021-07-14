from numpy import random
from RandomGenerator.RandomDecimal import Random_Decimal

def Random_Decimal_Seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        Random_decimal_seeded = Random_Decimal(start, end)
        return Random_decimal_seeded
    finally:
        random.set_state(state)
