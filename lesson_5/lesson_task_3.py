from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try:
    chrome.get("http://uitestingplayground.com/classattr/")
    for _ in range(3):
        blue_button = chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(2)
        

except Exception as ex:
    print(ex)
finally:
    chrome.quit()     



from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try:
    firefox.get("http://uitestingplayground.com/classattr/")
    for _ in range(3):
        blue_button = firefox.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button.click()
        sleep(2)
        

except Exception as ex:
    print(ex)
finally:
    firefox.quit()



 