import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from DataTypesPage import DataTypesPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_form_submission(driver):
    page = DataTypesPage(driver)
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

    page.fill_form(data)
    page.submit_form()

    # Проверяем подсветку полей
    for field_id in data.keys():
        field_class = page.get_field_class(field_id)
        assert "alert-success" in field_class.split(), f"Поле '{field_id}' должно быть подсвечено зеленым."

    # Проверяем подсветку поля Zip code
    zip_code_class = page.get_field_class("zip-code")
    assert "alert-danger" in zip_code_class.split(), "Поле 'zip-code' должно быть подсвечено красным."
