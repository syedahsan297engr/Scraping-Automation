from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import argparse

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the web page
url = 'https://www.temporary-mail.net/'  # Change this to the URL of your web page
driver.get(url)

try:
    # Click the button to trigger the dropdown
    button_xpath = '/html/body/section[1]/div/div/div[2]/div/div[2]/button'
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    button.click()

    # Wait for the dropdown <ul> to appear
    ul_xpath = '/html/body/section[1]/div/div/div[2]/div/div[2]/ul'
    ul_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ul_xpath)))

    # Get the HTML content of the <ul>
    ul_html = ul_element.get_attribute('outerHTML')

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(ul_html, 'html.parser')
    a_tags = soup.find_all('a')
    a_tag_contents = [a.get_text() for a in a_tags]
    # Extract and print the content of each <a> tag
    print(a_tag_contents)

finally:
    # Close the WebDriver
    driver.quit()
