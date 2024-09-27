import allure
from HW_9.Pages.DataBase import DataBase
from HW_9.Pages.Employee import Employer
from  HW_9.conftest import url

api = Employer("https://x-clients-be.onrender.com")
db = DataBase("postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")

@allure.title("Test Get List Employers")
@allure.description("This test validates the list of employers by comparing the database and API results.")
@allure.feature("Employer Management")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_list_employers():
    with allure.step("Creating test company in database"):
        db.create_company('Lili test', 'cool_company')

    with allure.step("Getting the last company ID from the database"):
        max_id = db.last_company_id()

    with allure.step("Deleting any previous employer data"):
        db.delete_employer(max_id)

    with allure.step("Creating a new employer in the test company"):
        db.create_employer(max_id, "Lili", "Mironova", 800400500)

    with allure.step("Fetching the list of employers from the database and API"):
        db_employer_list = db.get_list_employer(max_id)
        api_employer_list = api.get_list(max_id)

    with allure.step("Asserting that both lists contain the same number of employers"):
        assert len(db_employer_list) == len(api_employer_list)


@allure.title("Test Assertion Data")
@allure.description("This test asserts the data of a specific employer.")
@allure.feature("Employer Management")
@allure.severity(allure.severity_level.CRITICAL)
def test_assertion_data():
    with allure.step("Creating a test company in database"):
        db.create_company('Employer get ind company', 'new')

    with allure.step("Getting the last company ID from the database"):
        max_id = db.last_company_id()

    with allure.step("Creating a new employer in the test company"):
        db.create_employer(max_id, "Lili", "Mironova", "800400500")

    with allure.step("Fetching the employer ID from the database"):
        employer_id = db.get_employer_id(max_id)

    with allure.step("Getting the employer info from the API"):
        get_api_info = api.get_info(employer_id).json()

    with allure.step("Asserting that the API response matches the expected data"):
        assert get_api_info["firstName"] == "Lili"
        assert get_api_info["lastName"] == "Mironova"
        assert get_api_info["phone"] == "800400500"

    with allure.step("Cleaning up the test data from the database"):
        db.delete_employer(employer_id)
        


@allure.title("Test Adding New Employer")
@allure.description("This test adds a new employer and verifies the details.")
@allure.feature("Employer Management")
@allure.severity(allure.severity_level.CRITICAL)
def test_and_new_employer():
    with allure.step("Creating a test company in database"):
        db.create_company('Asi adding new employer', 'employer')

    with allure.step("Getting the last company ID from the database"):
        max_id = db.last_company_id()

    with allure.step("Creating a new employer in the test company"):
        db.create_employer(max_id, "Lili", "Mironova", "800400500")

    with allure.step("Fetching the employer details from the API"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]

    with allure.step("Asserting that the API response matches the expected details"):
        assert response["companyId"] == max_id
        assert response["firstName"] == "Lili"
        assert response["isActive"] == True
        assert response["lastName"] == "Mironova"

    with allure.step("Cleaning up the test data from the database"):
        db.delete_employer(employer_id)
        


@allure.title("Test Update User Info")
@allure.description("This test updates the information of an employer and verifies the changes.")
@allure.feature("Employer Management")
@allure.severity(allure.severity_level.CRITICAL)
def test_update_user_info():
    with allure.step("Creating a test company in database"):
        db.create_company('New updating company', 'test')

    with allure.step("Getting the last company ID from the database"):
        max_id = db.last_company_id()

    with allure.step("Creating a new employer in the test company"):
        db.create_employer(max_id, "Lili", "Mironova", "800400500")

    with allure.step("Fetching the employer ID from the database"):
        employer_id = db.get_employer_id(max_id)

    with allure.step("Updating the employer information in the database"):
        db.update_employer_info("Dima", employer_id)

    with allure.step("Getting the employer info from the API"):
        get_api_info = (api.get_info(employer_id)).json()

    with allure.step("Asserting that the API response matches the updated details"):
        assert get_api_info["firstName"] == "Dima"
        assert get_api_info["lastName"] == "Mironova"
        assert get_api_info["isActive"] == True

    with allure.step("Cleaning up the test data from the database"):
        db.delete_employer(employer_id)
        