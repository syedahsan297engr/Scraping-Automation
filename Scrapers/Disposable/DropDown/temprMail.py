from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to get content from a specified attribute
def get_drop_down(driver, xpath):
    output = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return output


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
    # Path to ChromeDriver (adjust as needed)
    chromedriver_path = "/usr/lib/chromium-browser/chromedriver"  # Change to your chromedriver path

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path
    # Open the website
    driver.get("https://tempr.email/")  # Change to your target website


    dropdown_xpath = '//*[@id="LoginDomainId"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    # Extract the text from each option
    dropdown_texts = [option.text for option in options]

    # Save the copied content to a text file
    append_list_to_file(dropdown_texts, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
