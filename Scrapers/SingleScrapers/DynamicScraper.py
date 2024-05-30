from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute):
    wait = WebDriverWait(driver)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Get the specified attribute from the element
    return element.get_attribute(attribute)

# Function to filter content extracting domains from mails
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

def save_to_file(content, file_path):
    try:
        # Read existing entries from the file to check for duplicates
        existing_entries = set()
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_entries = set(line.strip() for line in file)
        else:
            # If the file doesn't exist, create it and prepare to write content
            open(file_path, 'w').close()
        
        # Check if the content is already in the file
        if content not in existing_entries:
            with open(file_path, 'a') as file:
                if existing_entries:
                    file.write("\n")  # Optional newline for better formatting
                file.write(content)

            print(f"Content successfully appended to {file_path}")
        else:
            print(f"Content '{content}' already exists in {file_path}")

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def tempMailScraper(driver, fileName):
    driver.get("https://temp-mail.org/en/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = "//input[@id='mail']"

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFile = "dynamicDomains.txt"
    tempMailScraper(driver, outputFile) #its slow don't know why do this by handling button
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
