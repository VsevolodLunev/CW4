from abc import ABC, abstractmethod

import requests


class HhApi(ABC):
    """
    Абстрактный класс для получения вакансии с hh.ru
    """
    @abstractmethod
    def load_vacancies(self):
        pass


class HeadHunter(HhApi):
    """
    Класс для подключения к hh.ru
    """
    def __init__(self, keyword: str):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'Page': 0, 'per_page': 100}

    def load_vacancies(self) -> list[dict]:
        vacancies = []

        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            vacancies.extend(vacancies)
            self.params['page'] += 1

        return vacancies
