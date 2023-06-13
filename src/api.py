from src.abstract import API_Parser
import requests
import pprint


class HHApi(API_Parser):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword):
        """ Возвращает объект для работы с вакансиями"""
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

            # for vacancy in vacancies:
            #    vacancy["name"] = VDict[vacancy_title]
            #    vacancy_url = vacancy['alternate_url']
            #    if vacancy["salary"] is None:
            #        salary_min = None
            #        salary_max = None
            #    else:
            #        salary_min = vacancy["salary"]["from"]
            #        salary_max = vacancy["salary"]["to"]
            #    vacancy_requirement = vacancy["snippet"]["requirement"]
            #    vacancy_responsibility = vacancy["snippet"]["responsibility"]

        return vacancies


hh = HHApi()
h = hh.get_vacancies("python")
pprint.pprint(h)
