import pytest
from src.user_interactive import UserInteractive
from src.vacancy import Vacancy


@pytest.fixture()
def test():
    """
    Текстура создает 10 экземпляров тестовых вакансий
    """
    test = UserInteractive("name")
    test_list =[]
    for i in range(10):
        vac = Vacancy(
            name=f"testname {i}",
            area=f"testarea {i}",
            salary=i * 1000,
            url=f"testurl {i}",
            snippet=f"testsnippet {i}")
        test_list.append(vac)
    test.vacancies_list = test_list
    return test


def test_get_top_n_from_salary(test):
    """
    Тестирование варианта, где на вход метода подается пустой список
    """
    assert UserInteractive.get_top_n_for_salary(test, 0) == []


def test_get_top_n_from_salary_2(test):
    """
    Тестирование варианта, где на вход метода подаются 5 вакансий
    """
    assert len(UserInteractive.get_top_n_for_salary(test, 5)) == 5


def test_get_top_n_from_salary_3(test):
    """
    Тестирование зарплаты в последней тестовой вакансии
    """
    assert UserInteractive.get_top_n_for_salary(test, 1)[0].salary == 9000