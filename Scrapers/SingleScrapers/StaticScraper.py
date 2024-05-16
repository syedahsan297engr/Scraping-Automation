from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Function to get a specific element's value using XPath
def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def get_element_value_2(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.get_attribute("value")

# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Get the specified attribute from the element
    return element.get_attribute(attribute)

# Function to save content to a text file
def save_to_file(content, file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        mode = "a"  # Append mode if file exists
    else:
        mode = "w"  # Write mode to create file if it doesn't exist

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")  # Optional newline for better formatting
        file.write(content)




def fakeMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.fakemail.net/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

def InboxKittenScraper(driver, fileName):
    # Open the desired website
    driver.get("https://inboxkitten.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="div-domain"]'

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

def mailCatchScraper(driver, fileName):
    driver.get("http://mailcatch.com")  # Change to your target website

    # XPath for the button to click
    email_xpath = "//*[@id='copy-button']"

    # Wait for a moment to ensure the action completes
    time.sleep(0.1)  # Adjust as needed based on website response time

    # Get the copied content
    copied_content = get_element_attribute(driver, email_xpath, "data-clipboard-text")
    # Save the copied content to a text file
    save_to_file(copied_content, fileName)
    return


def minuteInboxScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.minuteinbox.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

def tempailScraper(driver, fileName):
    driver.get("https://tempail.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="eposta_adres"]'

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value_2(driver, input_xpath)
    print(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

def tempMailScraper(driver, fileName):
    driver.get("https://temp-mail.org/en/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = "//input[@id='mail']"

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")

    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

def tenMinMailScraper(driver, fileName):
    driver.get("https://10minutemail.net/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="fe_text"]'

    time.sleep(10)
    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    # Save the retrieved content to a text file
    save_to_file(content,fileName)
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFile = "staticDomains.txt"
    fakeMailScraper(driver, outputFile)
    InboxKittenScraper(driver, outputFile)
    mailCatchScraper(driver, outputFile)
    minuteInboxScraper(driver, outputFile)
    #tempailScraper(driver, outputFile) #require captacha solve it later
    tempMailScraper(driver, outputFile)
    tenMinMailScraper(driver, outputFile)
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
