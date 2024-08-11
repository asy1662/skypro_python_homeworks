from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настраиваем драйвер Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Переходим на сайт
    driver.get('http://uitestingplayground.com/textinput')

    # Находим поле ввода и вводим текст "SkyPro"
    input_field = driver.find_element(By.ID, 'newButtonName')
    input_field.send_keys('SkyPro')

    # Находим синюю кнопку и нажимаем на нее
    blue_button = driver.find_element(By.ID, 'updatingButton')
    blue_button.click()

    # Небольшая задержка, чтобы убедиться, что текст обновился


    # Получаем текст кнопки и выводим его в консоль
    button_text = blue_button.text
    print(button_text)  # Должно напечатать "SkyPro"

finally:
    # Закрываем браузер
    driver.quit()