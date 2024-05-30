# //*[@id="email"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
# Function to set up WebDriver
def setup_webdriver(chromedriver_path):
    # Initialize Chrome WebDriver with the correct path
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)

# Function to get a specific element's value using XPath
def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

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

# Main execution
def main():
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Change to your chromedriver path

    # Initialize the WebDriver
    # driver = setup_webdriver(chromedriver_path)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the desired website
    driver.get("https://www.minuteinbox.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    print(content)
    # Save the retrieved content to a text file
    save_to_file(content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
