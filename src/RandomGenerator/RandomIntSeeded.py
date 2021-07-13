from numpy import random
from RandomGenerator.RandomInt import random_int

def random_int_seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rand_integer_seeded = random_int(start, end)
        return rand_integer_seeded
    finally:
        random.set_state(state)