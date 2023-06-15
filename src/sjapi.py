import json
import requests
import pprint
from src.vacancy import Vacancy
from src.abstract import API_Parser


class SJApi(API_Parser):
    def __init__(self):
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, keyword):

        sj_list = []

        url = self.url
        params = {"count": 10, "page": None,
                  "keyword": keyword, "archive": False, }
        headers = {'Host': 'api.superjob.ru',
                   'X-Api-App-Id': "v3.r.137614390.20db844b570be75c7e4732fdbba6f34b1f802bcd.d8a6caebb4a52e2f2d3aeecac89d18bd48209ee5",
                   'Authorization': 'Bearer r.000000010000001.example.access_token',
                   'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        vacancies = data.get("objects")
        for vacancy in vacancies:
            title = vacancy['profession']
            url = vacancy['link']
            if vacancy['payment_from']:
                salary_min = vacancy['payment_from']
            else:
                salary_min = None
            if vacancy['payment_to']:
                salary_max = vacancy['payment_to']
            else:
                salary_max = None
            description = vacancy['candidat']

            sj_dict = {'title': title,
                       'url': url,
                       'salary_min': salary_min,
                       'salary_max': salary_max,
                       'description': description}
            sj_list.append(sj_dict)

        return sj_list

    def make_json_file(self, sj_list):
        with open("vacancies_file.json", "w", encoding='UTF-8') as file:
            json.dump(sj_list, file, indent=4, ensure_ascii=False)


a = SJApi()
b = a.get_vacancies("python")
a.make_json_file(b)
