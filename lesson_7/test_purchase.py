import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="module")
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield browser
    browser.quit()

def test_purchase(driver):
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_to_cart([
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ])

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info("Имя", "Фамилия", "12345")

    total_amount = checkout_page.get_total_amount()

    assert total_amount == "$58.29", f"Expected total to be $58.29 but was {total_amount}"
