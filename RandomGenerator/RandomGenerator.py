from RandomGenerator.RandomDecimal import Random_decimal
from RandomGenerator.RandomDecList import random_dec_list
from RandomGenerator.RandomDecimalSeeded import Random_decimal_seeded
from RandomGenerator.RandomInt import random_int
from RandomGenerator.RandomIntegerList import random_integer_list
from RandomGenerator.RandomIntSeeded import random_int_seeded

class Random:

    result = 0

    def random_decimal(self, start, end):
        self.result = Random_decimal(start, end)
        return self.result

    def random_dec_list(self, start, end, length, seed):
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