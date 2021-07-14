from numpy import random
from RandomGenerator.RandomDecimal import Random_decimal

def Random_decimal_seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        Random_decimal_seeded = Random_decimal(start, end)
        return Random_decimal_seeded
    finally:
        random.set_state(state)
