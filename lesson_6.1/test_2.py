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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Set delay value to 45
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Assert delay input is set correctly
    assert delay_input.get_attribute('value') == "45", "Delay value not set properly"

    # Press buttons 7, +, 8, =
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button.strip()}']"))
        )
        button_element.click()

    # Wait for the result to appear in the screen
    result = WebDriverWait(driver, 70).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    screen_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text.strip()
    print(f"Screen text is: {screen_text}")

    # Assert the result is 15
    assert screen_text == "15", f"Expected result to be 15, but got '{screen_text}'"
