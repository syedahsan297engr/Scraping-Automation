from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to set up WebDriver
def setup_webdriver(chromedriver_path):
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service)

# Function to get content from a specified attribute
def get_drop_down(driver, xpath):
    output = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return output


#for inboxes
def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def handle_form(driver, xpath):
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return dropdown

def append_list_to_file(text_list, file_path):
    try:
        # Read existing entries from the file to check for duplicates
        existing_entries = set()
        try:
            with open(file_path, 'r') as file:
                existing_entries = set(line.strip() for line in file)
        except FileNotFoundError:
            # If the file doesn't exist, create it
            open(file_path, 'w').close()  # Create the file

        # Open the specified file in append mode (this will create the file if it doesn't exist)
        with open(file_path, 'a') as file:
            # Write each item only if it is not already in the file
            for item in text_list:
                if item not in existing_entries:
                    file.write(item + '\n')  # Adding newline after each entry
                    existing_entries.add(item)

        print(f"Data successfully appended to {file_path}")

    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

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
    
# 4
def guerillaScraper(driver, fileName):
    # Open the website
    driver.get("https://www.guerrillamail.com/")  # Change to your target website
    dropdown_xpath = '//*[@id="gm-host-select"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    # Save the copied content to a text file
    append_list_to_file(dropdown_texts, fileName)
    return

# 3
def inboxesScraper(driver, fileName):
    #inboxes drop down
    driver.get("https://getnada.com")  # Change to your target website
    button_selector = "/html/body/div[1]/main/div/div/div/div[1]/button"
    get_button_clicked(driver, button_selector)
    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/form/div/div[2]/select"
    dropdown = handle_form(driver, dropdown_selector)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    # Extract the text from each option
    dropdown_texts = [option.text for option in options[1:]]
    # Save the copied content to a text file
    append_list_to_file(dropdown_texts, fileName)
    return

# 17
def temprMailScraper(driver, fileName):
    driver.get("https://tempr.email/")  # Change to your target website
    dropdown_xpath = '//*[@id="LoginDomainId"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    # Extract the text from each option
    dropdown_texts = [option.text for option in options]

    # Save the copied content to a text file
    append_list_to_file(dropdown_texts, fileName)
    return

# 19
def emailFakeScraper(driver, fileName):
    driver.get("https://emailfake.com/")  # Change to your target website

    button_selector = "/html/body/div[3]/div/div/div/div[3]"
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
    append_list_to_file(dropdown_texts, fileName)
    return

# 20
def generatorMailScraper(driver, fileName):
    driver.get("https://generator.email/")  # Change to your target website

    button_selector = "/html/body/div[3]/div/div/div/div[3]"
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
    append_list_to_file(dropdown_texts, fileName)
    return

# 21
def temporaryMailNetScraper(driver, fileName):
    # Open the website
    driver.get("https://www.fakemailgenerator.net/")  # Change to your target website

    button_selector = "/html/body/section[1]/div/div/div[2]/div/div[2]/button"
    get_button_clicked(driver, button_selector)

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/section[1]/div/div/div[2]/div/div[2]/ul"
    dropdown = handle_form(driver, dropdown_selector)


    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "a")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return

# 22
def fakeMailGeneratorScraper(driver, fileName):
    # Open the website
    driver.get("http://www.fakemailgenerator.com")  # Change to your target website

    button_selector = '/html/body/div[1]/div[1]/div[1]/div[1]/div/div/button'
    get_button_clicked(driver, button_selector)

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[1]/div[1]/div[1]/div[1]/div/div/ul/li"
    dropdown = handle_form(driver, dropdown_selector)


    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "a")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return

# 23
def mailFakeScraper(driver, fileName):
    driver.get("https://mail-fake.com/")  # Change to your target website

    button_selector = "/html/body/div[3]/div/div/div/div[3]"
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
    append_list_to_file(dropdown_texts, fileName)
    return

# 24
def fakeTempMailScraper(driver, fileName):
    driver.get("https://faketempmail.com/")  # Change to your target website

    button_selector = "/html/body/div/div/div[1]/div[3]/div/div/div/div/div/div/aside[1]/ul/li[1]/div/button[1]"
    get_button_clicked(driver, button_selector)

    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div/div/div[1]/div[3]/div/div/div/div/div/div/aside[1]/ul/li[1]/div/ul"
    dropdown = handle_form(driver, dropdown_selector)


    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "span")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]

    # Save the copied content to a text file
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return

# 25
def instantMailScraper(driver, fileName):
    driver.get("https://instant-email.org/")  # Change to your target website

    dropdown_xpath = '//*[@id="domain"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    
    # Save the copied content to a text file
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return

# 29
def mailGenScraper(driver, fileName):
    driver.get("https://mailgen.biz/")  # Change to your target website

    dropdown_xpath = '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/form[1]/div/div/div[1]/div[1]/input'
    get_button_clicked(driver, dropdown_xpath)
    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/form[1]/div/div/div[1]/div[2]/div"
    dropdown = handle_form(driver, dropdown_selector)


    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "a")
    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    # Save the copied content to a text file
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return

# 30
def trashMailScraper(driver, fileName):
    driver.get("https://www.trash-mail.com/new-address/")  # Change to your target website

    dropdown_xpath = '//*[@id="form-domain-new-id"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")

    # Extract the text from each option
    dropdown_texts = [option.text for option in options]
    
    # Save the copied content to a text file
    append_list_to_file(filter_content(dropdown_texts), fileName)
    return



# Main execution logic
def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path
    outputFileName = "dropdowns.txt"
    # guerillaScraper(driver, outputFileName)
    # temprMailScraper(driver, outputFileName)
    # emailFakeScraper(driver, outputFileName)
    # generatorMailScraper(driver, outputFileName)
    # temporaryMailNetScraper(driver, outputFileName)
    # fakeMailGeneratorScraper(driver, outputFileName)
    # mailFakeScraper(driver, outputFileName)
    # fakeTempMailScraper(driver, outputFileName)
    # instantMailScraper(driver, outputFileName)
    # mailGenScraper(driver, outputFileName)
    trashMailScraper(driver, outputFileName)
    # inboxesScraper(driver, outputFileName) #takes little more time to scrap
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
