from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver (using Chrome as an example)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://getnada.com")

try:
    # Click the button to open the form (replace the selector with the correct one for your case)
    button_selector = "/html/body/div[1]/main/div/div/div/div[1]/button"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_selector))).click()

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/form/div/div[2]/select"
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, dropdown_selector)))

    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]

    print("Dropdown options:", dropdown_texts)

finally:
    # Always close the driver after finishing the script
    driver.quit()
