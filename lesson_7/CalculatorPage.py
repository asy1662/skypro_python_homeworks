from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    def set_delay(self, delay_time):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_time))

    def press_button(self, button_text):
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text.strip()}']"))
        )
        button_element.click()

    def get_result(self):
        screen_locator = (By.CSS_SELECTOR, "div.screen")
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(screen_locator, "15")
        )
        result_element = self.driver.find_element(*screen_locator)
        return result_element.text.strip()
