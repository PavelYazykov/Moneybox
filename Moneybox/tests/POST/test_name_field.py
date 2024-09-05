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


@allure.epic('POST /api/v1/moneybox/ Проверка поля name')
class TestName:

    @allure.description('1 символ')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'М', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'М'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('19 символов')
    def test_02(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумум', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'мумумумумумумумумум'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('20 символов')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'мумумумумумумумумуму', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'мумумумумумумумумуму'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Цифры (0123456789)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, '0123456789', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == '0123456789'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Кириллица (Счёт)')
    def test_05(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Счёт', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Счёт'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Латиница (Moneybox)')
    def test_06(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Moneybox', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Moneybox'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Пробел')
    def test_07(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Мой счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Нижнее подчеркивание')
    def test_08(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, 'Мой_счет', currency_id, amount, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля goal"""
        with allure.step('Проверка значения поля goal'):
            result_text = post_result.text
            data = json.loads(result_text)
            assert data['data']['wallet']['name'] == 'Мой_счет'
            print('Значение поля соответствует введенному')

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')
