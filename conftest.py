import pytest
from Moneybox.methods.auth import Auth
from Moneybox.methods.checking import Checking


@pytest.fixture()
def auth_fixture():
    result = Auth.auth()
    Checking.check_statuscode(result, 200)
    check = result.json()
    access_token = check.get('access_token')
    return access_token
