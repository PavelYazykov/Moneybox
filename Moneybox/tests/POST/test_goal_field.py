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


@allure.epic('POST /api/v1/moneybox/ Проверка поля goal')
class TestGoal:

    @allure.description('Значение целое число = 1')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 1, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['goal'] == '1.00'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Значение вещественное число = 0.01')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, 0.01, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['goal'] == '0.01'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')
