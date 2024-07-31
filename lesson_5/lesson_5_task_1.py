
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try:
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        firefox.find_element(By.XPATH, "//button[text()='Add Element']").click()
        sleep(0.5)

    firefox_delete_buttons = firefox.find_elements(By.XPATH, "//button[text()='Delete']")

    print(f"Размер списка кнопок 'Delete' в Chrome: {len(firefox_delete_buttons)}")


finally:
    firefox.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrom = webdriver.Chrome()

try:
    chrom.get("http://the-internet.herokuapp.com/add_remove_elements/")

    for _ in range(5):
        chrom.find_element(By.XPATH, "//button[text()='Add Element']").click()
        sleep(0.5)

    chrom_delete_buttons = chrom.find_elements(By.XPATH, "//button[text()='Delete']")

    print(f"Размер списка кнопок 'Delete' в Chrome: {len(chrom_delete_buttons)}")


finally:
    chrom.quit()


 
 