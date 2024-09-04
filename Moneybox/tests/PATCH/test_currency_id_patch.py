import json

import allure

from Moneybox.methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.checking import Checking

moneybox_id = 410
to_date = '2024-12-30'
goal = 1000
name = 'name'
currency_id = 2
is_archived = False


@allure.epic('PATCH /api/v1/moneybox/{moneybox_id}/ Проверка поля currency_id')
class TestCurrencyPatch:

    @allure.description('Существующий id')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """PATCH запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, to_date, goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле"'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['wallet']['currency_id'] == currency_id
            print('Значение поля currency_id сответствует введенному значению')

