from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import argparse
from bs4 import BeautifulSoup
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
    time.sleep(10)
    input_xpath = '//*[@id="trsh_mail"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "crazymailing.com", filePath)
    return

# 48
def kukuMailScraper(driver, filePath):
    driver.get("https://m.kuku.lu/index.php")
    time.sleep(5)
    input_xpath = '/html/body/div[1]/div[3]/div/div/div[8]/div[4]/div/div[1]/div/div[1]/a/div/span[2]'
    # input_xpath = '//*[@id="area_mailaddr_5ebb0d1cafdb9009a7ae313b42046a69"]'
    #//*[@id="area_mailaddr_5ebb0d1cafdb9009a7ae313b42046a69"]
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "kuku.lu", filePath)
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

def proMailNetScraper2(driver, filePath):
    driver.get("https://verifymail.io/domain/promail9.net")  
    dropdown_xpath = '/html/body/div[3]/section[2]/div[1]/div/div/div[1]/div/div[2]/div[6]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "promail9.net", filePath)
    return

def proMailNetScraper(driver, filePath):
    try:
        driver.get("https://verifymail.io/domain/promail9.net")
        # Fetch the page content using the Selenium WebDriver
        page_source =  driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Use CSS selectors to locate the specific section
        div = soup.select_one('body > div:nth-of-type(3) > section:nth-of-type(2) > div:nth-of-type(1) > div > div > div:nth-of-type(1) > div > div:nth-of-type(2) > div:nth-of-type(6) > span')

        if div:
            # Fetch all <a> tags within the specified section
            a_tags = div.find_all('a')

            # Extract the content (text) of each <a> tag
            a_texts = [a.get_text() for a in a_tags]

            save_list_to_csv(a_texts, "promail9.net", filePath)
        else:
            pass 
    except Exception as e:
        print(f"Error processing the webpage: {e}")

    return 

def parse_arguments():
    parser = argparse.ArgumentParser(description='InboxKitten Scraper')
    parser.add_argument('outputFilePath', type=str, help='Path to the output CSV file')
    return parser.parse_args()

# Main execution
def main():
    args = parse_arguments()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFilePath = args.outputFilePath
    # crazyMailScraper(driver, outputFilePath)
    # kukuMailScraper(driver, outputFilePath)
    proMailNetScraper(driver, outputFilePath)
    # mailCheckAiScraperUpdated(driver, outputFilePath) #this one to run as it will give you updated domains above will scrap one time
    # tempMailScraper(driver, outputFilePath) #takes time You can get the same data from above scraper very fast
    driver.quit()

if __name__ == "__main__":
    main()
