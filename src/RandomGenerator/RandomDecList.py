from numpy import random

def Random_Dec_List(start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        dec_list = random.uniform(start, end, length)
        return dec_list
    finally:
        random.set_state(state)

#https://www.geeksforgeeks.org/finally-keyword-in-python/