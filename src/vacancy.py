import json
from src.api import HHApi


class Vacancy:
    def __init__(self, vacancy_title, vacancy_url, requirements, salary_min=None, salary_max=None):
        self.vacancy_title = vacancy_title
        self.vacancy_url = vacancy_url
        self.requirements = requirements


