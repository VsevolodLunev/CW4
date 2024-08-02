import json
import os.path
from abc import ABC, abstractmethod


class FileWork(ABC):
    """
    Абстрактный класс для записи в файл
    """

    def __init__(self):
        pass

    @abstractmethod
    def read_file(self):
        """
        Чтение файла
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Запись файла
        """
        pass

    @abstractmethod
    def delete_file(self):
        """
        Удаление файла
        """
        pass


class WorkWithJason(ABC):
    """
    Класс для записи в json-файл
    """

    def __init__(self):
        self.file_name = ""
        self.abs_path = os.path.abspath("data/vacancies.json")

    def read_file(self) -> None:
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data: list[dict]) -> None:
        with open(self.abs_path, "w", encoding="utf-8") as file:
            """res = json.load(file)
            res.append(data)"""
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        return os.remove(self.abs_path)
