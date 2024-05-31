from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Function to get content from a specified attribute
def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def handle_form(driver, xpath):
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return dropdown

def append_list_to_file(text_list, file_path):
    try:
        # Open the specified file in append mode
        with open(file_path, 'a') as file:
            # Write each item on a new line
            for item in text_list:
                file.write(item + '\n')  # Adding newline after each entry

        print(f"Data successfully appended to {file_path}")

    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Main execution logic
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path
    # Open the website
    driver.get("https://generator.email/")  # Change to your target website

    button_selector = "/html/body/div[3]/div/div/div[1]/div[3]"
    get_button_clicked(driver, button_selector)

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div"
    dropdown = handle_form(driver, dropdown_selector)


    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "p")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]

    # print("Dropdown options:", dropdown_texts)
    # Save the copied content to a text file
    append_list_to_file(dropdown_texts, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
