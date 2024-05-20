from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
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
iframe = driver.find_element(By.XPATH, '//*[@id="ifdoms"]')
driver.switch_to.frame(iframe)

# Get the HTML content of the iframe
iframe_html = driver.find_element(By.XPATH, '/html/body').get_attribute('outerHTML')

# Print the HTML content
# print(iframe_html)

# Parse the HTML
soup = BeautifulSoup(iframe_html, 'html.parser')

# Find the div with class 'lstdom'
lstdom_div = soup.find('div', class_='lstdom')

# Extract the inner div contents and store them in a list
inner_divs_content = [div.text.strip() for div in lstdom_div.find_all('div')]

# Print the list of inner div contents
print(inner_divs_content)

# Close the browser
driver.quit()