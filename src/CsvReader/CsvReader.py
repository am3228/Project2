import csv
from pathlib import Path

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class Csv_Reader:
    data = []

    def __init__(self, filepath):
        self.data = []
        relative = Path(filepath)
        absolutepath = relative.absolute()
        with open(absolutepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_class(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects