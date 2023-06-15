import json


class JSONSaver:

    def __init__(self):
        self.path = "../src/vacancies_file.json"

    def get_data(self):
        with open(self.path, encoding='UTF-8') as file:
            data_json = file.read()
            data = json.loads(data_json)
        return data

    def filter_by_min_salary(self, data):
        pass













