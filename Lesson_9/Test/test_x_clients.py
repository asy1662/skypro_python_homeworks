import pytest
from Lesson_9.Pages.DataBase import DataBase
from Lesson_9.Pages.Employee import Employer


api= Employer(" https://x-clients-be.onrender.com")
db= DataBase("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

def test_get_list_employers():
    db.create_company('Asi test','cool_company') 
    max_id = db.last_company_id()
    
    db.delete_employer(max_id , "Asi", "Letova",86667788)
    db_employer_iist = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_iist)== len(api_employer_list)
    responce = (api.get_list(max_id))[0]
    employer_id = responce[id]
    db.delete_employer(employer_id)
    db.delete(max_id)

def test_assertion_data():
    db.create_company('Empoyer get ind company', 'nwe')
    max_id = db.last_company_id()
    db.create_company(max_id, "Asi", "Letova",100200300 )
    employer_id = db.get_employer_id(max_id)
    get_api_info = {api.get_info(employer_id)}.json
    assert get_api_info["firstName"]== "Asi"
    assert get_api_info["firstName"]== "Letova"
    assert get_api_info["firstName"]== "100200300"
    db.delete_employer(employer_id)
    db.delete(max_id)
    
def test_and_nwe_employer():
    db.create_company('Asi adding nwe employer','employer')
    max_id = db.last_company_id()
    db.create_company(max_id, "Asi", "Letova",100200300 )
    response = (api.get_list(max_id))[0]
    employer_id = response[id]
    assert response ["company_id"]== max_id
    assert response["firstName"]== "Asi"
    assert response["isActive"]== True
    assert response["lastName"] == "Letova"
    db.delete_employer(employer_id)
    db.delete(max_id)

def test_update_user_info():
    db.create_company('Nwe updating company', 'test')
    max_id = db.last_company_id()
    db.create_company(max_id,  "Asi", "Letova",100200300 )
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Dima" ,employer_id)
    get_api_info = (api.get_info (employer_id)).json()
    assert get_api_info["firstName"] == "Dima"
    assert get_api_info["lastName"] == "Letova"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)

    
    
    





    

    

    

