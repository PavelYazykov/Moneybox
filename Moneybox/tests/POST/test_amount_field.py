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


@allure.epic('POST /api/v1/moneybox/ Проверка поля amount')
class TestAmount:

    @allure.description('Создание копилки со значением 0')
    def test_01(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, amount, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля amount"""
        with allure.step('Проверка значения поля amount'):
            result_text = post_result.text
            data = json.loads(result_text)
            print(data['data']['wallet']['amount'])
            assert data['data']['wallet']['amount'] == '0'

        """Удаление копилки"""
        with allure.step('Удаление копилки'):
            moneybox_id = data['data']['id']
            MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
            print('Копилка удалена')

    @allure.description('Поле отсутствует')
    def test_02(self, auth_fixture):  # Тест будет падать

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(
            to_date, goal, name, currency_id, None, access_token
        )

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля amount"""
        with allure.step('Проверка значения поля amount'):
            result_text = post_result.text
            data = json.loads(result_text)
            print(data['data']['wallet']['amount'])
            assert data['data']['wallet']['amount'] is None

    @allure.description('Целое число')
    def test_03(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, 100, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля amount"""
        with allure.step('Проверка значения поля amount'):
            result_text = post_result.text
            data = json.loads(result_text)
            print(data['data']['wallet']['amount'])
            assert data['data']['wallet']['amount'] == '100'

        # """Удаление копилки"""
        # with allure.step('Удаление копилки'):
        #     moneybox_id = data['data']['id']
        #     MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        #     print('Копилка удалена')

    @allure.description('Вещественное число (5,5)')
    def test_04(self, auth_fixture):

        """Авторизация"""
        access_token = auth_fixture

        """POST запрос"""
        post_result = MoneyboxMethods.create_moneybox(to_date, goal, name, currency_id, 5.5, access_token)

        """Проверка статус кода"""
        Checking.check_statuscode(post_result, 201)
        print(post_result.text)

        """Проверка значения поля amount"""
        with allure.step('Проверка значения поля amount'):
            result_text = post_result.text
            data = json.loads(result_text)
            print(data['data']['wallet']['amount'])
            assert data['data']['wallet']['amount'] == '5.5'

        # """Удаление копилки"""
        # with allure.step('Удаление копилки'):
        #     moneybox_id = data['data']['id']
        #     MoneyboxMethods.delete_moneybox(moneybox_id, access_token)
        #     print('Копилка удалена')

