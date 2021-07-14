from numpy import random
from RandomGenerator.RandomInt import Random_Int

def Random_int_seeded(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rand_integer_seeded = Random_Int(start, end)
        return rand_integer_seeded
    finally:
        random.set_state(state)