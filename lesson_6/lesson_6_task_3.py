from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Переход на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Добавим проверку текущего состояния элемента с текстом
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.ID, "text")))
        print("Current text:", element.text)
    except:
        print("Element with ID 'text' not found within 10 seconds")

    # Ожидание загрузки текста "Done"
    wait = WebDriverWait(driver, 50)
    try:
        done = wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done"))
        print("Text 'Done' is present on the page.")
    except:
        print("Text 'Done' was not found within 50 seconds.")

    # Получение значения атрибута src у 3-й картинки и вывод его в консоль
    try:
        third_image = driver.find_element(By.XPATH, "(//div[@class='image-wrapper']/img)[3]")
        src_value = third_image.get_attribute("src")

        print("Third image src:", src_value)  # Вывод значения в консоль
    except:
        print("Third image not found.")

finally:
    driver.quit()