from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  # to handle delays if needed
import os
# Function to set up WebDriver
def setup_webdriver(chromedriver_path):
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)

# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Get the specified attribute from the element
    return element.get_attribute(attribute)

# Function to save content to a text file
# Function to write or append content to a text file
def write_or_append_to_file(content, file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        mode = "a"  # Append mode if file exists
    else:
        mode = "w"  # Write mode to create file if it doesn't exist

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")  # Optional newline for better formatting
        file.write(content)

# Main execution logic
def main():
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Change to your chromedriver path

    # Initialize the WebDriver
    # driver = setup_webdriver(chromedriver_path)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  #no need to setup chrome driver by yourself
    # Open the website
    driver.get("http://mailcatch.com")  # Change to your target website

    # XPath for the button to click
    email_xpath = "//*[@id='copy-button']"

    # Wait for a moment to ensure the action completes
    time.sleep(0.1)  # Adjust as needed based on website response time

    # XPath for the element containing copied content (assuming it's copied to another field)
    # Example: where the content might be placed after clicking the copy button
    # content_xpath = "//input[@id='mail']"  # Adjust to the actual element that holds the copied content

    # Get the copied content
    copied_content = get_element_attribute(driver, email_xpath, "data-clipboard-text")
    print(copied_content)
    # Save the copied content to a text file
    write_or_append_to_file(copied_content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
