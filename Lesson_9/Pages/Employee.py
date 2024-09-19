import requests
import json
from Lesson_9.conftest import url



path = '/employee/'

class Company:
    def __init__(self, url=url):
        self.url = url


#создание компании
class Company:
    def __init__(self, url=url):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(self.url + '/company', headers=headers, json=body)
        return response.json()
    
    def last_active_company_id(self):
        active_params = {"active":"true"}
        response = requests.get(self.url +'/company',params= active_params)
        return response.json()[-1]['id']
    


class Employer:
    def __init__(self, base_url):
        self.base_url = base_url
    # список сотрудников компании
    def get_employees(self,company_id):
        response = requests.get("f{self.base_url} + '/employee", params={"company":company_id})
        return response

    # добавление сотрудника
    def add_employee(self, token, employee_data):
        headers = {'x-client-token': token}
        response = requests.post("f{self.base_url} + '/employee", headers=headers, json=employee_data)
        return response

    # получение информации
    def get_employee_by_id(self, employee_id):
        response = requests.get("f{self.base_url}/employee/{employee_id}")
        return response

    # изменение информации
    def update_employee(self, token, employee_id, employee_data):
        headers = {'x-client-token': token}
        response = requests.patch("f{self.base_url}/employee/{employee_id}",headers=headers,json =employee_data)
        return response

