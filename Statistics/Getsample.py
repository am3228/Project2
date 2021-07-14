from random import random

def Getsample(data, sample_size):
    random_values = random.choices(data, k=sample_size)
    return random_values