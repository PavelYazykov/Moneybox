import json

import allure


class Checking:
    """Проверки"""

    @staticmethod
    def check_statuscode(result, status_code):
        with allure.step('Проверка статус кода'):
            assert result.status_code == status_code
            print(f'Успешно статус код: {result.status_code}')

