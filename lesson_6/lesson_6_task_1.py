from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(level=logging.INFO)

try:
    logging.info("Initializing Chrome browser.")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        browser.get('http://uitestingplayground.com/ajax')
        logging.info("Navigated to http://uitestingplayground.com/ajax")

        button = browser.find_element(By.ID, 'ajaxButton')
        logging.info("Found the button with ID 'ajaxButton'. Clicking it.")
        button.click()

        wait = WebDriverWait(browser, 20)
        logging.info("Waiting for the success alert to become visible.")
        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success')))

        alert_text = alert.text
        logging.info(f"Alert text: {alert_text}")

    except Exception as e:
        logging.exception("An error occurred during the browser operations.")
    finally:
        logging.info("Closing the browser.")
        browser.quit()

except Exception as e:
    logging.exception("Failed to initialize the browser.")
