import pytest
from Lesson_9.Pages.DataBase import DataBase
from Lesson_9.Pages.Employee import Employer
from Lesson_9.conftest import url


api= Employer(" https://x-clients-be.onrender.com")
db= DataBase("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

def test_get_list_employers():
    db.create_company('Lili test', 'cool_company')
    max_id = db.last_company_id()  # Получение ID новосозданной компании
    db.delete_employer(max_id)# Создание сотрудника в тестовой компании
    db.create_employer(max_id, "Lili", "Mironova", 800400500)# Получение списков работодателей из базы данных и API
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list) # Убедитесь, что оба списка содержат равное количество сотрудников


def test_assertion_data():
    # Создание тестовой компании
    db.create_company('Employer get ind company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Lili", "Mironova", "800400500")
    employer_id = db.get_employer_id(max_id)
    get_api_info = api.get_info(employer_id).json()

    # Проверка, что ответ API соответствует ожидаемым данным

    assert get_api_info["firstName"] == "Lili"
    assert get_api_info["lastName"] == "Mironova"
    assert get_api_info["phone"] == "800400500"
    db.delete_employer(employer_id)
   # db.delete(max_id) не удаляется'DataBase' object has no attribute 'delete'

def test_and_nwe_employer():
    db.create_company('Asi adding nwe employer','employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Lili", "Mironova", "800400500")
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    assert response ["companyId"]== max_id
    assert response["firstName"]== "Lili"
    assert response["isActive"]== True
    assert response["lastName"] == "Mironova"
    db.delete_employer(employer_id)
   # db.delete(max_id)

def test_update_user_info():
    db.create_company('Nwe updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Lili", "Mironova", "800400500")
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Dima" ,employer_id)
    get_api_info = (api.get_info (employer_id)).json()
    assert get_api_info["firstName"] == "Dima"
    assert get_api_info["lastName"] == "Mironova"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
   # db.delete(max_id)