from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def login_test(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('tomsmith')
    sleep(1)

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('SuperSecretPassword!')
    sleep(1)

    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()
    sleep(2)

    driver.quit()

driver = webdriver.Chrome()
login_test(driver)

driver = webdriver.Firefox()
login_test(driver)