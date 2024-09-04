import allure
import requests
from Moneybox.methods.http_methods import HttpMethods


base_url = 'https://budget-test.god-it.ru/api'


class MoneyboxMethods:
    """Методы для тестрования Копилок"""

    @staticmethod
    def create_moneybox(to_date, goal, name, currency_id, amount, access_token):
        with allure.step('Создание копилки'):
            post_endpoint = '/api/v1/moneybox/'
            post_url = base_url + post_endpoint
            print(post_url)
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "amount": amount
                }
            }
            post_response = HttpMethods.post(post_url, body, access_token)
            return post_response

    @staticmethod
    def get_all_moneybox(access_token):
        with allure.step('Получение списка всех копилок'):
            get_endpoint = '/api/v1/moneybox/'
            get_url = base_url + get_endpoint
            print(get_url)
            get_response = HttpMethods.get(get_url, access_token)
            return get_response

    @staticmethod
    def get_one_moneybox(moneybox_id, access_token):
        with allure.step('Получение копилки по id'):
            get_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            get_url = base_url + get_endpoint + id_moneybox
            print(get_url)
            get_response = HttpMethods.get(get_url, access_token)
            return get_response

    @staticmethod
    def change_moneybox(moneybox_id, to_date, goal,  name, currency_id, is_archived, access_token):
        with allure.step('Внесение изменений в копилку'):
            patch_endpoint = '/api/v1/moneybox/'
            id_moneybox = str(moneybox_id) + "/"
            body = {
                "to_date": to_date,
                "goal": goal,
                "wallet": {
                    "name": name,
                    "currency_id": currency_id,
                    "is_archived": is_archived}
            }
            patch_url = base_url + patch_endpoint + id_moneybox
            print(patch_url)
            patch_response = HttpMethods.patch(patch_url, body, access_token)
            return patch_response

    @staticmethod
    def delete_moneybox(moneybox_id, access_token):
        with allure.step('Удаление копилки'):
            delete_endpoint = '/api/v1/moneybox/'
            moneybox_id = str(moneybox_id) + '/'
            delete_url = base_url + delete_endpoint + moneybox_id
            delete_result = HttpMethods.delete(delete_url, access_token)
            return delete_result
