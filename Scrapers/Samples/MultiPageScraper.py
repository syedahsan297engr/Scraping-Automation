#/html/body/section/div/div[2]/div[1]/div[1]/div/code/span/span
#/html/body/section/div/div[2]/div[2]/div[1]/div/code/span/span
#/html/body/section/div/div[2]/div[20]/div[1]/div/code/span/span
#/html/body/section/div/div[2]/div[6]/div[1]/div/code/span/span
#on next page.
#/html/body/section/div/div[2]/div[20]/div[1]/div/code/span/span

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from bs4 import BeautifulSoup

# Function to get a specific element's value using XPath
def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def get_element_value_2(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.get_attribute("value")

def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def get_button_clicked_2(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
    return
# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Get the specified attribute from the element
    return element.get_attribute(attribute)

# Function to filter content extracting domains from mails
def filter_content(content):
    if isinstance(content, list):
        filtered_list = []
        for item in content:
            if "@" in item:
                filtered_list.append(item.split("@")[-1])
            else:
                filtered_list.append(item)
        return filtered_list
    elif isinstance(content, str):
        if "@" in content:
            return content.split("@")[-1]
        else:
            return content
    else:
        raise ValueError("Content must be a string or a list of strings")


def append_list_to_file(text_list, file_path):
    try:
        # Read existing entries from the file to check for duplicates
        existing_entries = set()
        try:
            with open(file_path, 'r') as file:
                existing_entries = set(line.strip() for line in file)
        except FileNotFoundError:
            # If the file doesn't exist, create it
            open(file_path, 'w').close()  # Create the file

        # Open the specified file in append mode (this will create the file if it doesn't exist)
        with open(file_path, 'a') as file:
            # Write each item only if it is not already in the file
            for item in text_list:
                if item not in existing_entries:
                    file.write(item + '\n')  # Adding newline after each entry
                    existing_entries.add(item)

        print(f"Data successfully appended to {file_path}")

    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")


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
        append_list_to_file(domains, fileName)
        domains = []
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFile = "oneScrap.txt"
    mailCheckAiScraper(driver, outputFile)
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
