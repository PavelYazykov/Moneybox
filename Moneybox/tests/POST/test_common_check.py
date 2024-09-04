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


@allure.epic('POST /api/v1/moneybox/ Создание персональных транзакций общие проверки')
class TestCommon:

    @allure.description('Создание новой копилки с валидными значениями (авторизованный пользователь)')
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

        """Проверка наличия обязательных полей"""
        with allure.step('Проверка наличия обязательных полей'):
            result_text = post_result.text
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
