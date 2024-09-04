import json

import allure

from Moneybox.methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.checking import Checking

to_date = '2024-12-30'
name = 'name'
goal = 1000
currency_id = 2
amount = 0


@allure.epic('POST /api/v1/moneybox/ Проверка поля to_date')
class TestToDate:

    @allure.description('Создание копилки с валидной датой')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['to_date'] == '2024-12-30'
            print('Значение поля соответствует введенному')
