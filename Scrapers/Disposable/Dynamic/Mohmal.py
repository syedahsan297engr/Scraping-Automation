#/html/body/div[1]/main/div/div/div/div[1]/h1/span[2]/div/div[2]/span

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time  # to handle delays if needed
import os
from webdriver_manager.chrome import ChromeDriverManager


# Function to get content from a specified attribute
def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text


def append_list_to_file(text_list, file_path):
    try:
        # Open the specified file in append mode
        with open(file_path, 'a') as file:
            # Write each item on a new line
            for item in text_list:
                file.write(item)  # Adding newline after each entry

        print(f"Data successfully appended to {file_path}")

    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")



# Main execution logic
def main():
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Change to your chromedriver path

    # Initialize the WebDriver
    # driver = setup_webdriver(chromedriver_path)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path
    # Open the website
    driver.get("https://www.mohmal.com/en")  # Change to your target website

    button_selector = '//*[@id="rand"]'
    get_button_clicked(driver, button_selector)

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    xpath = "/html/body/div/div[1]/div[2]/div[3]/div[1]"
    content = get_element_value(driver, xpath)

    print(content)
    # Get all the option elements from the dropdown
    append_list_to_file(content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
