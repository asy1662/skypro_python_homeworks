from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_ids):
        for product_id in product_ids:
            self.driver.find_element(By.ID, product_id).click()