from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from bs4 import BeautifulSoup

def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def crazyMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.crazymailing.com/")  # Change to your target website
    time.sleep(2) # wait for the content to appear
    button_xpath = "/html/body/section[1]/div[2]/div/div/div/div[1]/button"
    get_button_clicked(driver, button_xpath)
    content = driver.execute_script("""
        return (navigator.clipboard.readText().then(function(text) {
            return text;
        }).catch(function(err) {
            console.error('Failed to read clipboard contents: ', err);
            return null;
        }));
    """)
    print(content)
    return