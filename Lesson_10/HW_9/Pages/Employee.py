import requests
import json
import allure
from HW_9.conftest import url



path = '/employee/'

class Company:
    def __init__(self, url=url):
        self.url = url


#создание компании
    @allure.step("Создание компании")
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/company', headers=headers, json=body)
        return response.json()
    @allure.step("Получение id последней активной компании")
    def last_active_company_id(self):
        active_params = {"active":"true"}
        response = requests.get(self.url +'/company',params= active_params)
        return response.json()[-1]['id']
    


class Employer:
    def __init__(self, url=url):
        self.url = url
    @allure.step("Получение списка сотрудников компании")
    def get_list(self, company_id: int):
        company = {'company':company_id}
        response = requests.get(self.url + '/employee', params=company)
        return response.json()

    @allure.step("Добавление нового сотрудника")
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/employee', headers=headers, json=body)
        return response.json()

    @allure.step("Получение информации о сотруднике")
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response

    @allure.step("Изменение информации о сотруднике")
    def chanqe_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers, json=body)
        return response