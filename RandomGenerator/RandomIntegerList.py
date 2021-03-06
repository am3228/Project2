from numpy import random

def Random_Integer_List(start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        integer_list = random.randint(start, end, length)
        return integer_list
    finally:
        random.set_state(state)

#https://www.geeksforgeeks.org/finally-keyword-in-python/