from src.RandomGenerator.RandomDecimal import Random_decimal
from src.RandomGenerator.RandomDecList import random_dec_list
from src.RandomGenerator.RandomDecimalSeeded import Random_decimal_seeded
from src.RandomGenerator.RandomInt import random_int
from src.RandomGenerator.RandomIntegerList import random_integer_list
from src.RandomGenerator.RandomIntSeeded import random_int_seeded

class Random_Generator:
    result = 0
    data = []

    def __init__(self):
        pass

    def Random_Decimal(self, start, end):
        self.result = Random_decimal(start, end)
        return self.result

    def Random_Dec_List(self, start, end, length, seed):
        self.result = random_dec_list(start, end, length, seed)
        return self.result

    def random_decimal_seeded(self, start, end, seed):
        self.result = Random_decimal_seeded(start, end, seed)
        return self.result

    def random_int(self, start, end):
        self.result = random_int(start, end)
        return self.result

    def random_integer_list(self, start, end, length, seed):
        self.result = random_integer_list(start, end, length, seed)
        return self.result

    def random_int_seeded(self, start, end, seed):
        self.result = random_int_seeded(start, end, seed)
        return self.result