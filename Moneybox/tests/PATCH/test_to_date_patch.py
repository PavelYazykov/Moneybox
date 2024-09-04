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


@allure.epic('PATCH /api/v1/moneybox/{moneybox_id}/ Проверка поля to_date')
class TestToDate:

    @allure.description('Изменить на валидную дату')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """PATCH запрос"""
        result_patch = MoneyboxMethods.change_moneybox(
            moneybox_id, '2024-11-30', goal, name, currency_id, is_archived, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_patch, 200)
        print(result_patch.text)

        """Проверка значения в изменяемом поле"""
        with allure.step('Проверка значения в изменяемом поле'):
            result_text = result_patch.text
            data = json.loads(result_text)
            assert data['data']['to_date'] == '2024-11-30'
            print('Значение поля to_date соответствует введенному')

