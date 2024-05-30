from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Function to set up WebDriver
def setup_webdriver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Function to extract inner div contents from an iframe
def extract_inner_divs_content(driver, iframe_xpath):
    # Switch to the iframe
    iframe = driver.find_element(By.XPATH, iframe_xpath)
    driver.switch_to.frame(iframe)

    # Get the HTML content of the iframe
    iframe_html = driver.find_element(By.XPATH, '/html/body').get_attribute('outerHTML')

    # Parse the HTML
    soup = BeautifulSoup(iframe_html, 'html.parser')

    # Find the div with class 'lstdom'
    lstdom_div = soup.find('div', class_='lstdom')

    # Extract the inner div contents and store them in a list
    inner_divs_content = [div.text.strip() for div in lstdom_div.find_all('div')]

    return inner_divs_content

# Function to save content to a text file
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

# Main function
def main():
    # Initialize the WebDriver
    driver = setup_webdriver()

    # Open the website
    driver.get("https://yopmail.com/alternate-domains")

    # XPath for the iframe containing the div with class 'lstdom'
    iframe_xpath = '//*[@id="ifdoms"]'

    # Extract inner div contents from the iframe
    inner_divs_content = extract_inner_divs_content(driver, iframe_xpath)

    # Print the extracted content
    # print(inner_divs_content)

    # Save the content to a text file
    append_list_to_file(inner_divs_content, "copied_content.txt")

    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
