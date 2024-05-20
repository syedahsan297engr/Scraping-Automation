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

# Set up options for Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome for no GUI

# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path

# Open the website
driver.get("https://yopmail.com/alternate-domains")  # Use the actual URL

# Switch to the iframe to access its contents
iframe = driver.find_element(By.CLASS_NAME, '.lstdom')
driver.switch_to.frame(iframe)

# Get the HTML content of the iframe
iframe_html = driver.find_element(By.XPATH, '/html/body').get_attribute('outerHTML')

# Print the HTML content
print(iframe_html)

# Close the browser
driver.quit()
