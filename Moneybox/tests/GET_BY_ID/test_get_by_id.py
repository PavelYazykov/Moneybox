import json
from Moneybox.methods.auth import Auth
from Moneybox.methods.moneybox_methods import MoneyboxMethods
from Moneybox.methods.checking import Checking
import allure

moneybox_id = 410


@allure.epic('GET /api/v1/moneybox/{moneybox_id}/ Получение списка копилок по id')
class TestGetById:

    @allure.description('Существующим ID (авторизованный пользователь)')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """Get запрос"""
        result_get = MoneyboxMethods.get_one_moneybox(
            moneybox_id, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(result_get, 200)
        print(result_get.text)

        """Проверка id копилки"""
        with allure.step('Проверка id копилки'):
            result_text = result_get.text
            data = json.loads(result_text)
            assert data['data']['id'] == 410
            print('id копилки соответствует введенному')
