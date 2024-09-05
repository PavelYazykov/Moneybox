import json

import allure

from Moneybox.methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.checking import Checking

to_date = '2024-12-30'
goal = 1000
name = 'name'
currency_id = 2
amount = 0


@allure.epic('POST /api/v1/moneybox/ Проверка поля currency_id')
class TestCurrencyId:

    @allure.description('Существующий id')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка поля currency_id"""
        with allure.step('Проверка поля currency_id'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['currency_id'] == currency_id
            print('Значение поля currency_id соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')
