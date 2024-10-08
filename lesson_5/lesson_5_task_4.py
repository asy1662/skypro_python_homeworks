import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Работа с Chrome
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)
modal_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))

time.sleep(3)
close_button.click()
time.sleep(2)

driver.quit()

# Работа с Firefox
driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)
modal_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))

time.sleep(3)
close_button.click()
time.sleep(2)

driver.quit()