import pytest
import requests
from Lesson_9.conftest import url



# Пример фикстуры для получения токена для аутентификации в тестах.
@pytest.fixture()
def get_token(username='donatello', password='does-machines'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(f"{url}/auth/login", json=log_pass)
    token = resp_token.json().get('userToken')
    return token