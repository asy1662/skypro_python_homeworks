from selenium import webdriver
from time import sleep


try:
    driver = webdriver.Chrome()
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

    for i in range(3):
        blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
        blue_button.click()
        count += 1

        sleep(2)

    print(count)
except Exception as ex:
    print(ex)
finally:
    driver.quit()


try:
    driver = webdriver.Firefox()
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
    blue_button.click()

    for i in range(3):
        blue_button = driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]')
        blue_button.click()
        count += 1

        sleep(2)

    print(count)
except Exception as ex:
    print(ex)
finally:
    driver.quit()
