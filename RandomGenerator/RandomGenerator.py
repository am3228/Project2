from RandomGenerator.RandomDecimal import Random_Decimal
from RandomGenerator.RandomDecList import Random_Dec_List
from RandomGenerator.RandomDecimalSeeded import Random_Decimal_Seeded
from RandomGenerator.RandomInt import Random_Int
from RandomGenerator.RandomIntegerList import Random_Integer_List
from RandomGenerator.RandomIntSeeded import Random_Int_Seeded

class Random_Generator:
    result = 0
    data = []

    def __init__(self):
        pass

    def Random_Decimal(self, start, end):
        self.result = Random_Decimal(start, end)
        return self.result

    def Random_Dec_List(self, start, end, length, seed):
        self.result = Random_Dec_List(start, end, length, seed)
        return self.result

    def random_decimal_seeded(self, start, end, seed):
        self.result = Random_Decimal_Seeded(start, end, seed)
        return self.result

    def random_int(self, start, end):
        self.result = Random_Int(start, end)
        return self.result

    def random_integer_list(self, start, end, length, seed):
        self.result = Random_Integer_List(start, end, length, seed)
        return self.result

    def random_int_seeded(self, start, end, seed):
        self.result = Random_Int_Seeded(start, end, seed)
        return self.result