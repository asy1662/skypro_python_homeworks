from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataTypesPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, data):
        for field_name, value in data.items():
            field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, field_name))
            )
            field.send_keys(value)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

    def get_field_class(self, field_id):
        field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, field_id))
        )
        return field.get_attribute("class")
