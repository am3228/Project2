from random import random

def Get_sample(data, sample_size):
    random_values = random.choices(data, k=sample_size)
    return random_values