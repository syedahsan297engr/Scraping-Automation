from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from utilities import get_element_value, get_element_value_2, get_element_attribute, save_to_csv, get_button_clicked
import pyperclip
# 1
def tempMailScraper(driver, filePath):
    driver.get("https://temp-mail.org/en/")
    input_xpath = "//input[@id='mail']"
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "temp-mail.org", filePath)
    return

# 28
def crazyMailScraper(driver, filePath):
    driver.get("https://www.crazymailing.com/")
    time.sleep(7)
    input_xpath = '//*[@id="trsh_mail"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "crazymailing.com", filePath)
    return

# 48
def kukuMailScraper(driver, filePath):
    driver.get("https://m.kuku.lu/index.php")
    input_xpath = '/html/body/div[1]/div[3]/div/div/div[8]/div[4]/div/div[1]/div/div[1]/a/div/span[2]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "kuku.lu", filePath)
    return



# 59
def tenMinMailScraper(driver, filePath):
    driver.get("https://10minutemail.com/")
    button_xpath = '//*[@id="mail_address"]'
    time.sleep(7)
    content = get_element_value_2(driver, button_xpath)
    save_to_csv(content, "10minutemail.com", filePath)
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFilePath = "Sample.csv"
    crazyMailScraper(driver, outputFilePath)
    kukuMailScraper(driver, outputFilePath)
    tenMinMailScraper(driver, outputFilePath)
    tempMailScraper(driver, outputFilePath) #takes time
    driver.quit()

if __name__ == "__main__":
    main()
