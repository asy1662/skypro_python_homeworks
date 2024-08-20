import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    # Установите задержку в 45 секунд
    calculator_page.set_delay(45)

    # Нажмите кнопки для вычисления: 7 + 8 =
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        calculator_page.press_button(button)

    # Получите и проверьте результат
    result = calculator_page.get_result()
    assert result == "15", f"Expected result to be 15, but got '{result}'"
