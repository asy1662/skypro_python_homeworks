import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Обновленные пути импорта
from HW_7.pages.login_page import LoginPage
from HW_7.pages.products_page import ProductsPage
from HW_7.pages.cart_page import CartPage
from HW_7.pages.checkout_page import CheckoutPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

@allure.feature("Покупка продуктов")
@allure.title("Проверка покупки продуктов")
@allure.description("Тест на покупку продуктов и проверку итоговой суммы.") 
@allure.severity(allure.severity_level.BLOCKER)
def test_purchase(driver):  # Уберите 'self' из параметров функции
    with allure.step("Открыть сайт Saucedemo"):
        driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    with allure.step("Войти под стандартным пользователем"):
        login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    with allure.step("Добавить выбранные продукты в корзину"):
        products_page.add_to_cart([
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ])

    cart_page = CartPage(driver)
    with allure.step("Перейти к оформлению заказа"):
        cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    with allure.step("Заполнить информацию о заказе"):
        checkout_page.fill_checkout_info("Имя", "Фамилия", "12345")

    with allure.step("Проверить общую сумму заказа"):
        total_amount = checkout_page.get_total_amount()
        assert total_amount == "$58.29", f"Expected total to be $58.29 but was {total_amount}"
