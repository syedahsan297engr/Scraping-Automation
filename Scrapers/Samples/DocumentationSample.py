from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#driver = webdriver.Chrome()
#sudo apt install chromium-chromedriver
chrome_service = Service("/usr/lib/chromium-browser/chromedriver")  # Change this to your chromedriver path
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
driver.quit()