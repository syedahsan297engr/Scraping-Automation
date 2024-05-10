from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os

# Function to set up WebDriver
def setup_webdriver(chromedriver_path):
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)

# Function to get text content from an element by class name
def get_element_text_by_class(driver, class_name, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    # Get the text content from the element
    return element.text

# Function to write or append content to a text file
def write_or_append_to_file(content, file_path):
    with open(file_path, "a") as file:  # Open in append mode
        file.write("\n")  # Optional newline for better formatting
        file.write(content)

# Main execution logic
def main():
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Adjust to your actual ChromeDriver path

    # Initialize the WebDriver
    driver = setup_webdriver(chromedriver_path)

    # Open the website
    driver.get("https://getnada.com")  # Change to your target website

    # Reload the page once
    driver.refresh()

    # Class name to locate the element
    class_name = "finished-typing"

    # Use WebDriverWait to ensure the element is accessible
    copied_content = get_element_text_by_class(driver, class_name)

    # Output the copied content
    print("Copied Content:", copied_content)

    # Write or append to the text file without overwriting existing content
    write_or_append_to_file(copied_content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
