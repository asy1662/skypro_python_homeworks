import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from HW_7.CalculatorPage import CalculatorPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()
@allure.title("Тест: Проверка калькулятора")
@allure.description("Проверка выполнения арифметической операции 7 + 8")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    with allure.step("Установить задержку в 45 секунд"):
        calculator_page.set_delay(45)

    # Нажмите кнопки для вычисления: 7 + 8 =
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        with allure.step(f"Нажать кнопку: {button}"):
         calculator_page.press_button(button)

    # Получите и проверьте результат
    with allure.step("Получить результат"):
     result = calculator_page.get_result()
    with allure.step("Проверить результат"):
     assert result == "15", f"Expected result to be 15, but got '{result}'"
