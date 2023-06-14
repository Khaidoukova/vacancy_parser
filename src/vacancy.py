class Vacancy:
    def __init__(self, vacancy_title, vacancy_url, requirements, salary_min=None, salary_max=None):
        self.vacancy_title = vacancy_title
        self.vacancy_url = vacancy_url
        self.requirements = requirements
        self.salary_min = salary_min
        self.salary_max = salary_max

    def __str__(self):
        return f'Название вакансии: {self.vacancy_title} ' \
               f'Ссылка на вакансию: {self.vacancy_url} ' \
                f'Требования к соискателю: {self.requirements} ' \
                f'Минимальная зарплата {self.salary_min} руб. ' \
                f'Максимальная зарплата {self.salary_max} руб. ' \

