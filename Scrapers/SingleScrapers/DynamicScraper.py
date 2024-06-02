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
    wait = WebDriverWait(driver, timeout)
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

def save_to_file(content, file_path):
    try:
        # Read existing entries from the file to check for duplicates
        existing_entries = set()
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_entries = set(line.strip() for line in file)
        else:
            # If the file doesn't exist, create it and prepare to write content
            open(file_path, 'w').close()
        
        # Check if the content is already in the file
        if content not in existing_entries:
            with open(file_path, 'a') as file:
                if existing_entries:
                    file.write("\n")  # Optional newline for better formatting
                file.write(content)

            print(f"Content successfully appended to {file_path}")
        else:
            print(f"Content '{content}' already exists in {file_path}")

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# 1
def tempMailScraper(driver, fileName):
    driver.get("https://temp-mail.org/en/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = "//input[@id='mail']"

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 28
def crazyMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.crazymailing.com/")  # Change to your target website
    time.sleep(7) # wait for the content to appear
    input_xpath = '//*[@id="trsh_mail"]'
    # Get the value from the specified element using this javascript code
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return


# 37
def anonBoxScraper(driver, fileName):
    # Open the desired website
    driver.get("https://anonbox.net/en/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div[2]/dl/dd[2]/p'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return


# 48
def kukuMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://m.kuku.lu/index.php")  # Change to your target website
    input_xpath = '/html/body/div[1]/div[3]/div/div/div[8]/div[4]/div/div[1]/div/div[1]/a/div/span[2]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 56
# 5
def fakeMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.fakemail.net/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 59
def tenMinMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://10minutemail.com/")  # Change to your target website
    button_xpath = '//*[@id="mail_address"]'
    time.sleep(1)
    content = get_element_value_2(driver, button_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFile = "dynamicDomains.txt"
    crazyMailScraper(driver,outputFile)
    anonBoxScraper(driver, outputFile)
    kukuMailScraper(driver, outputFile)
    fakeMailScraper(driver, outputFile)
    tenMinMailScraper(driver, outputFile)
    # tempMailScraper(driver, outputFile) #its slow don't know why do this by handling button
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
