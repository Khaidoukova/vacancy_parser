from abc import ABC, abstractmethod


class API_Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass
