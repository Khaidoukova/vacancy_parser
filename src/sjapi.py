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
        params = {"count": 100, "page": None,
                  "keyword": keyword, "archive": False, }

        headers = {"X-Api-App-Id": "v3.r.137614390.20db844b570be75c7e4732fdbba6f34b1f802bcd.d8a6caebb4a52e2f2d3aeecac89d18bd48209ee5"}
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        vac = data.get()

        return vac.text

a = SJApi
print(a.get_vacancies("python"))




