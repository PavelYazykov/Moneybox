import json

from Moneybox.methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.checking import Checking
import allure


@allure.epic('GET /api/v1/moneybox/ Получение списка всех копилок')
class TestGetAll:

    @allure.description('Получение списка всех копилок (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_all_moneybox(access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print(result_get.text)





