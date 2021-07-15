from numpy import random
from src.RandomGenerator.RandomDecimal import Random_Decimal

def Random_Decimal_Seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        Random_Dec_Seeded = Random_Decimal(start, end)
        return Random_Dec_seeded
    finally:
        random.set_state(state)
