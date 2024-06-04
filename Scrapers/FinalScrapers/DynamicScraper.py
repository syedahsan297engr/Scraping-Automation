from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from utilities import get_element_value, get_element_value_2, get_element_attribute, save_to_csv, save_list_to_csv, get_drop_down

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

# added from prev records
def mailCheckAiScraper(driver, fileName):
    domains = []
    base_url = "https://www.mailcheck.ai/provider/temp-mail.org"
    for page in range(1,  56):
        url = f"{base_url}?page={page}"
        driver.get(url)
        #got that page now handle different x paths
        totalDivs = 20
        if page == 55:
            totalDivs = 6
        for divNumber in range(1,totalDivs+1):
            xpath = f"/html/body/section/div/div[2]/div[{divNumber}]/div[1]/div/code/span/span"
            content = get_element_value(driver, xpath)
            if content:
                domains.append(content)
        save_list_to_csv(domains,"mailcheck.ai", fileName)
        domains = []
    return

def mailCheckAiScraperUpdated(driver, fileName):
    domains = []
    base_url = "https://www.mailcheck.ai/provider/temp-mail.org"
    for page in range(1,  3):
        url = f"{base_url}?page={page}"
        driver.get(url)
        #got that page now handle different x paths
        totalDivs = 20
        for divNumber in range(1,totalDivs+1):
            xpath = f"/html/body/section/div/div[2]/div[{divNumber}]/div[1]/div/code/span/span"
            content = get_element_value(driver, xpath)
            if content:
                domains.append(content)
        save_list_to_csv(domains,"mailcheck.ai", fileName)
        domains = []
    return

def proMailNetScraper(driver, filePath):
    driver.get("https://verifymail.io/domain/promail9.net")  
    dropdown_xpath = '/html/body/div[3]/section[2]/div[1]/div/div/div[1]/div/div[2]/div[6]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "promail9.net", filePath)
    return

#//*[@id="file-free_email_provider_domains-txt-LC3"]
def freeEmailProvidersGitHubScraper(driver, filePath):
    driver.get("https://gist.github.com/mpyw/6b59ffbe517da9cccbf40db9aa30d09b")  
    domains = []
    # total 9683 records are there on github
    for id in range (1, 9683):
        xpath = f'//*[@id="file-free_email_provider_domains-txt-LC{id}"]'
        currDomain = get_element_value(driver, xpath)
        domains.append(currDomain)
    # print(len(domains)) #5886 #20815
    save_list_to_csv(domains, "github.mpyw", filePath)
    return


# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFilePath = "/home/ahsan/Desktop/Scraping-Automation/Documents/disposable-domains.csv"
    crazyMailScraper(driver, outputFilePath)
    kukuMailScraper(driver, outputFilePath)
    tenMinMailScraper(driver, outputFilePath)
    mailCheckAiScraper(driver, outputFilePath)
    proMailNetScraper(driver, outputFilePath)
    mailCheckAiScraper(driver, outputFilePath) #this one to run as it will give you updated domains above will scrap one time
    tempMailScraper(driver, outputFilePath) #takes time
    freeEmailProvidersGitHubScraper(driver, outputFilePath)
    driver.quit()

if __name__ == "__main__":
    main()
