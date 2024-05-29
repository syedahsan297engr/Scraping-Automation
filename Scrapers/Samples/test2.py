from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Function to set up WebDriver
def setup_webdriver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to get text content of all options in a dropdown
def get_dropdown_options(driver, xpath, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
    dropdown_element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    options = dropdown_element.find_elements(By.TAG_NAME, "option")
    return [option.text for option in options]

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
        file.write("\n".join(content))

# Main execution logic
def main():
    # Initialize the WebDriver
    driver = setup_webdriver()

    # Open the website
    driver.get("https://emailfake.com/")

    # XPath for the dropdown element
    dropdown_xpath = '/html/body/div[3]/div[1]/div/div/div[2]/div[2]/div/div'

    # Wait for a moment to ensure the action completes
    time.sleep(0.1)  # Adjust as needed based on website response time

    # Get the dropdown options content
    dropdown_options = get_dropdown_options(driver, dropdown_xpath)
    print(dropdown_options)
    # Save the dropdown options content to a text file
    #write_or_append_to_file(dropdown_options, "dropdown_options.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
