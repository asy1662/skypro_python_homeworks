from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys('1000')
    sleep(2)
    input_field.clear()
    input_field.send_keys('999')

except Exception as ex:
    print(ex)

finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/inputs")

    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys('1000')
    sleep(2)
    input_field.clear()
    input_field.send_keys('999')

except Exception as ex:
    print(ex)

finally:
    driver.quit()
