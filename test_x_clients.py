import pytest
import requests
import json
from Lesson_8.constants import X_client_URL
from Lesson_8.Pages.Employee import Employer,Company


employer = Employer()
company = Company()



def test_authorization(get_token: json.Any):
    token = get_token
    assert token is not None
    assert isinstance(token,str)

def test_getcompany_id():
    company_id = company.last_active_company_id
    assert company_id is not None
    assert str(company_id).isdigit
       
def test_add_employer(get_token: json.Any):
    token=str(get_token)
    com_id= company.last_active_company_id()
    body_employer= {
        "id": 0,
  "firstName": "Dima",
  "lastName": "Petrof",
  "middleName": "string",
  "companyId":  com_id,
  "email": "test@yandex.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-09-02T10:43:13.060Z",
  "isActive": True
    }
    nwe_employer_id=(employer.add_new(token,body_employer))['id']
    assert nwe_employer_id is not None
    assert str(nwe_employer_id).isdigit()

def test_get_employer ():
    com_id=company.last_active_company_id()
    list_employers= employer.get_list(com_id)
    assert isinstance(list_employers,list)

def test_change_employer_info(get_token: json.Any):
    token= str(get_token)
    com_id = company.last_active_company_id()
    body_employer= {
        "id": 0,
  "firstName": "Dima",
  "lastName": "Petrof",
  "middleName": "string",
  "companyId":  com_id,
  "email": "test@yandex.ru",
  "url": "string",
  "phone": "string",
  "birthdate": "2024-09-02T10:43:13.060Z",
  "isActive": True
    }
    just_employer = employer.add_new(token, body_employer)
    id= just_employer['id']
    body_change_employer = {
        "lastName": "Veselov",
          "email": "test3@yandex.ru",
          "url": "string",
          "phone": "string",
           "isActive": True
    }
    employer_changet = employer.chanqe_info(token,id,body_change_employer)
    assert employer_changet.status_code == 200





    


        
    

    




    




  









    