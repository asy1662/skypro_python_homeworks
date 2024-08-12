import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_purchase(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    try:
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))
        )
        print("First name input is present")
    except Exception as e:
        print(f"Timeout while waiting for the page to load. Exception: {e}")
        driver.save_screenshot('timeout_error.png')
        raise

    fields = {
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

    for field_name, value in fields.items():
        try:
            print(f"Looking for field: {field_name}")
            field = WebDriverWait(driver, 40).until(
                EC.visibility_of_element_located((By.NAME, field_name))
            )
            field.send_keys(value)
        except Exception as e:
            print(f"Could not find the field with name '{field_name}'. Exception: {e}")
            driver.save_screenshot(f'field_{field_name}_error.png')
            raise

    try:
        submit_button = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()
    except Exception as e:
        print(f"Could not find or click the submit button. Exception: {e}")
        driver.save_screenshot('submit_error.png')
        raise

    try:
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.CLASS_NAME, "was-validated"))
        )
        print("Form was validated")
    except Exception as e:
        print(f"Timeout while waiting for form validation. Exception: {e}")
        driver.save_screenshot('validation_timeout_error.png')
        raise

    for field_name in fields.keys():
        field = driver.find_element(By.NAME, field_name)
        if "is-valid" not in field.get_attribute("class").split():
            driver.save_screenshot(f'field_{field_name}_validation_error.png')
        assert "is-valid" in field.get_attribute("class").split(), f"Поле '{field_name}' должно быть подсвечено зеленым."

    try:
        zip_code_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "zip-code"))
        )
        if "is-invalid" not in zip_code_field.get_attribute("class").split():
            driver.save_screenshot('zip_code_validation_error.png')
        assert "is-invalid" in zip_code_field.get_attribute("class").split(), "Поле 'Zip code' должно быть подсвечено красным."
    except Exception as e:
        print(f"Failed to validate zip code field. Exception: {e}")
        driver.save_screenshot('zip_code_check_error.png')
        raise

    try:
        error_message = driver.find_element(By.CSS_SELECTOR, "[name='zip-code'] + .invalid-feedback")
        assert error_message.is_displayed(), "Сообщение об ошибке возле поля 'Zip code' должно отображаться."
    except Exception as e:
        print(f"Failed to find error message for zip code field. Exception: {e}")
        driver.save_screenshot('zip_code_error_message_error.png')
        raise
