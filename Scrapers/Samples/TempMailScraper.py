from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Set up the Chrome WebDriver (adjust the path to your downloaded chromedriver)
# sudo apt install chromium-chromedriver
chrome_service = Service("/usr/lib/chromium-browser/chromedriver")  # Change this to your chromedriver path
driver = webdriver.Chrome(service=chrome_service)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open the website
# driver = webdriver.Chrome()
driver.get("https://temp-mail.org/en/")  # Change to your target website

# Wait for the page to load and the element to be accessible
wait = WebDriverWait(driver, 10)  # 10 seconds timeout
input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='mail']")))

# Retrieve the value from the input field
content = input_element.get_attribute("value")

print(content)

# Close the WebDriver
driver.quit()
