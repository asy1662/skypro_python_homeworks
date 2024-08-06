from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    
    wait = WebDriverWait(driver, 50)
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='image-wrapper']/img)[4]")))

    
    third_image = driver.find_element(By.XPATH, "(//div[@class='image-wrapper']/img)[3]")

    src_value = third_image.get_attribute("src")
    if src_value:
        print("SRC attribute of the 3rd image: " + src_value)
    else:
        print("The 3rd image does not have an 'src' attribute.")

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
