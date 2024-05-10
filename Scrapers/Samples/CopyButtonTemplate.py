from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Function to set up WebDriver
def setup_webdriver(chromedriver_path):
    # Initialize Chrome WebDriver with the correct path
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)

# Function to get a specific element's value using XPath
def get_element_value(driver, xpath, timeout=10):
    # Wait for the element to be present and accessible
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Retrieve the value from the element
    return element.get_attribute("value")

# Function to save content to a text file
def save_to_file(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)

# Main execution
def main():
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Change to your chromedriver path

    # Initialize the WebDriver
    driver = setup_webdriver(chromedriver_path)

    # Open the desired website
    driver.get("https://temp-mail.org/en/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = "//input[@id='mail']"

    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)

    # Save the retrieved content to a text file
    save_to_file(content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
