import json
import pprint
from src.vacancy import Vacancy
from src.hhapi import HHApi
from src.sjapi import SJApi
from src.json_saver import JSONSaver

def main():


    print("Приветствую тебя, моя Госпожа! Что изволите искать?")
    keyword = input("Введите, пожалуйста, ключевое слово для поиска вакансий: ")
    vacancies_json = []
    hh = HHApi(keyword, 100)
    sj = SJApi(keyword, 100)
    for i in (hh, sj):
        v = i.get_vacancies()
        vacancies_json.extend(v)

    jsonsaver = JSONSaver(keyword=keyword, vacancy_list=vacancies_json)

    while True:
        user_input = input("1 - Вакансии с сайта Headhanter. \n"
              "2 - Вакансии с сайта SuperJob. \n"
              "3 - поиск на всех сайтах \n"
              "4 - выход \n")

        if user_input == "4":
            break

        elif user_input == "1":

            answer1 = input("Максимальное число вакансий для вывода на экран: ")
            vacancies_json = []
            hh = HHApi(keyword, answer1)
            v = hh.get_vacancies()
            vacancies_json.append(v)
            HHApi.make_json_file(v)
            Vacancy.vacancy_ex(vacancies_json)
            for item in Vacancy.all_vacancies:
                print(str(item))

        #answer2 = input("Введите, пожалуйста, город для поиска: ")
        #
        #keyword2 = keyword + " " + answer2



        elif answer1 == "2":
            vacancies_json = []
            sj = SJApi(keyword, answer3)
            v = sj.get_vacancies()
            vacancies_json.extend(v)
            Vacancy.vacancy_ex(vacancies_json)
            for item in Vacancy.all_vacancies:
                print(str(item))

        elif answer1 == "3":
            vacancies_json = []
            hh = HHApi(keyword2, answer3)
            sj = SJApi(keyword, answer3)
            for i in (hh, sj):
                v = i.get_vacancies()
                vacancies_json.extend(v)
                Vacancy.vacancy_ex(vacancies_json)
                for item in Vacancy.all_vacancies:
                    print(str(item))

        elif answer1 == "4":
            break




if __name__ == "__main__":
    main()













