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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")  # Fixed URL

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="first-name"]'))
        )
        print("First name input is present")
    except Exception as e:
        print(f"Timeout while waiting for the page to load. Exception: {e}")
        driver.save_screenshot('timeout_error.png')
        raise

    fields = {
        "First name": "Иван",
        "Last name": "Петров",
        "Address": "Ленина, 55-3",
        "Email": "test@skypro.com",
        "Phone": "+7985899998787",
        "City": "Москва",
        "Country": "Россия",
        "Job position": "QA",
        "Company": "SkyPro"
    }

    for field_name, value in fields.items():
        try:
            print(f"Looking for field: {field_name}")  # Debug info
            field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"input[placeholder='{field_name}']"))
            )
            field.send_keys(value)
        except Exception as e:
            print(f"Could not find the field with placeholder '{field_name}'. Exception: {e}")
            driver.save_screenshot(f'field_{field_name}_error.png')
            raise

    try:
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()
    except Exception as e:
        print(f"Could not find or click the submit button. Exception: {e}")
        driver.save_screenshot('submit_error.png')
        raise

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "was-validated"))
        )
        print("Form was validated")
    except Exception as e:
        print(f"Timeout while waiting for form validation. Exception: {e}")
        driver.save_screenshot('validation_timeout_error.png')
        raise

    for field_name in fields.keys():
        field = driver.find_element(By.CSS_SELECTOR, f"input[placeholder='{field_name}']")
        if "is-valid" not in field.get_attribute("class"):
            driver.save_screenshot(f'field_{field_name}_validation_error.png')
        assert "is-valid" in field.get_attribute("class"), f"Поле '{field_name}' должно быть подсвечено зеленым."

    zip_code_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Zip code']")
    if "is-invalid" not in zip_code_field.get_attribute("class"):
        driver.save_screenshot('zip_code_validation_error.png')
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле 'Zip code' должно быть подсвечено красным."