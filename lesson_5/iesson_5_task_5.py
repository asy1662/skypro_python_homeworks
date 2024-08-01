from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_input_field(driver):
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

# Test with Chrome
driver_chrome = webdriver.Chrome()
test_input_field(driver_chrome)

# Test with Firefox
driver_firefox = webdriver.Firefox()
test_input_field(driver_firefox)