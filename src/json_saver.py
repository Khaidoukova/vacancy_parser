import json
import pprint


class JSONSaver:

    def __init__(self):
        self.path = "../src/vacancies_file.json"

    def get_data(self):
        with open(self.path, encoding='UTF-8') as file:
            data_json = file.read()
            data = json.loads(data_json)
        return data

    def filter_by_min_salary(self):
        salary_min_list = []
        data = self.get_data()
        for i in data:
            if i['salary_min']:
                salary_min_list.append(i)
        salary_min_list = sorted(salary_min_list, key=lambda x: x['salary_min'], reverse=True)
        with open("filtered_list.json", "a", encoding='UTF-8') as file:
            json.dump(salary_min_list, file, indent=4, ensure_ascii=False)
            
    def filter_by_max_salary(self):
        salary_max_list = []
        data = self.get_data()
        for i in data:
            if i['salary_max']:
                salary_max_list.append(i)
        salary_max_list = sorted(salary_max_list, key=lambda x: x['salary_max'], reverse=True)
        return salary_max_list



n = JSONSaver()
nn = n.filter_by_min_salary()
pprint.pprint(nn)
