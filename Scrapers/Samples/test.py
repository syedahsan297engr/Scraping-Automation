from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time  # to handle delays if needed
import os
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path


try:
    # Open the website
    driver.get('https://www.mohmal.com/en')
    
    # Click the button identified by the XPath
    button = driver.find_element(By.XPATH, '//*[@id="rand"]')
    button.click()
    
    # Wait for the new page to load
    driver.implicitly_wait(10)  # Adjust the wait time as necessary

    # Scrape the content from the new page
    content = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[3]/div[1]')
    print(content.text)

finally:
    # Close the WebDriver
    driver.quit()
