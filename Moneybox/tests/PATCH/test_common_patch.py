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


@allure.epic('PATCH /api/v1/moneybox/{moneybox_id}/ Редактирование копилок, общие проверки')
class TestCommonPatch:

    @allure.description('С существующим ID и валидными значениями в полях (авторизованный пользователь')
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

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            result_text = result_patch.text
            data = json.loads(result_text)
            required_fields = {
                "data": {
                    "to_date": "2024-12-30",
                    "goal": "1000.00",
                    "wallet": {
                        "name": "My Goal_2",
                        "currency_id": 2,
                        "amount": "0"
                    }
                }
            }

            for field in required_fields:
                assert field in data, f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']:
                assert field in data['data'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')

            for field in required_fields['data']['wallet']:
                assert field in data['data']['wallet'], f"Отсутствует обязательное поле: {field}"
                print(f'Обязательное поле {field} присутствует')
