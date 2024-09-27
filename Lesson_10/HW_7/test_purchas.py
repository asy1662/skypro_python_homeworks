import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from  HW_7.DataTypesPage import DataTypesPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

@allure.feature("Форма с типами данных")
@allure.title("Заполнение и отправка формы с валидными данными")
@allure.description("Тест на заполнение и успешную отправку формы с правильными данными.")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission(driver):  # Уберите 'self' из параметров функции
       page = DataTypesPage(driver)

       with allure.step("Открытие страницы формы"):
           page.open()

       data = {
           "first-name": "Иван",
           "last-name": "Петров",
           "address": "Ленина, 55-3",
           "e-mail": "test@skypro.com",
           "phone": "+7985899998787",
           "city": "Москва",
           "country": "Россия",
           "job-position": "QA",
           "company": "SkyPro"
       }

       with allure.step("Заполнение формы"):
           page.fill_form(data)

       with allure.step("Отправка формы"):
           page.submit_form()

       with allure.step("Проверка, что все поля формы подсвечены зелёным"):
           for field_id in data.keys():
               field_class = page.get_field_class(field_id)
               assert "alert-success" in field_class.split(), f"Поле '{field_id}' должно быть подсвечено зелёным."

       with allure.step("Проверка подсветки поля Zip code"):
           zip_code_class = page.get_field_class("zip-code")
           assert "alert-danger" in zip_code_class.split()