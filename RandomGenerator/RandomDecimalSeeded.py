from numpy import random
from RandomGenerator.randomDecimal import random_decimal

def random_decimal_seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        randm_decimal_seeded = random_decimal(start, end)
        return randm_decimal_seeded
    finally:
        random.set_state(state)
