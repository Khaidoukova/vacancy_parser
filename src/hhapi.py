import json
import requests
import pprint
from src.abstract import API_Parser
from src.vacancy import Vacancy


class HHApi(API_Parser):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):

        v_dict = {}
        v_list = []

        url = self.url
        params = {
            "text": keyword,
            "per_page": 10,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items")
            for vacancy in vacancies:
                title = vacancy["name"]
                url = vacancy['alternate_url']
                if vacancy["salary"] is None:
                    salary_min = None
                    salary_max = None
                else:
                    salary_min = vacancy["salary"]["from"]
                    salary_max = vacancy["salary"]["to"]

                description = vacancy["snippet"]["requirement"]

                v_dict = {'title': title,
                          'url': url,
                          'salary_min': salary_min,
                          'salary_max': salary_max,
                          'description': description}

                v_list.append(v_dict)
            return v_list

        else:
            print("Ошибка подключения.")

    def make_json_file(self, v_list):
        with open("vacancies_file.json", "w", encoding='UTF-8') as file:
            json.dump(v_list, file, indent=4, ensure_ascii=False)


hh = HHApi()
h = hh.get_vacancies("python")
hh.make_json_file(h)

