from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from bs4 import BeautifulSoup

# Function to get a specific element's value using XPath
def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def get_element_value_2(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.get_attribute("value")

def get_button_clicked(driver, xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    return

def get_button_clicked_2(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
    return
# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute, timeout=10):
    wait = WebDriverWait(driver, timeout)  # Timeout in seconds
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


# Html parsing required for some cases
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

# 1
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

# 6
def mailCatchScraper(driver, fileName):
    driver.get("http://mailcatch.com")  # Change to your target website

    # XPath for the button to click
    email_xpath = "//*[@id='copy-button']"

    # Get the copied content
    content = get_element_attribute(driver, email_xpath, "data-clipboard-text")
    content = filter_content(content)
    # Save the copied content to a text file
    save_to_file(content, fileName)
    return

# 10
def tenMinMailScraper(driver, fileName):
    driver.get("https://10minutemail.net/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="fe_text"]'

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content,fileName)
    return

# 11
def minuteInboxScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.minuteinbox.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 12
def InboxKittenScraper(driver, fileName):
    # Open the desired website
    driver.get("https://inboxkitten.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="div-domain"]'

    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 13
def tempailScraper(driver, fileName):
    driver.get("https://tempail.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="eposta_adres"]'

    # Get the value from the specified element
    content = get_element_value_2(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return


# beautiful soup used for this
# 14
def yopMailScraper(driver, fileName):
    driver.get("https://yopmail.com/alternate-domains")

    # XPath for the iframe containing the div with class 'lstdom'
    iframe_xpath = '//*[@id="ifdoms"]'

    # Extract inner div contents from the iframe
    inner_divs_content = extract_inner_divs_content(driver, iframe_xpath)
    inner_divs_content = filter_content(inner_divs_content)
    # Save the content to a text file
    append_list_to_file(inner_divs_content, fileName)

    # Close the WebDriver
    driver.quit()
    return

# 31
def fakeeMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://fakeemail.co/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div/div/header/div/div/div/div[2]/div/div[2]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 32
def harikiriMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://harakirimail.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="randominboxLink"]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 34
def uroidScraper(driver, fileName):
    driver.get("https://uroid.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="eposta_adres"]'

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content,fileName)
    return

# 35
def tenMinMailScraper(driver, fileName):
    # Open the desired website
    driver.get("https://10minutemail.com/")  # Change to your target website
    button_xpath = '//*[@id="mail_address"]'
    time.sleep(1)
    content = get_element_value_2(driver, button_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return


# 43
def eyePasteScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.eyepaste.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div[1]/div[2]/div/h1'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return


# 46
def einWegScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.einweg-email.com")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="my-address"]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 47
def mail1aScraper(driver, fileName):
    # Open the desired website
    driver.get("https://mail1a.de/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div[2]/div[1]/div[1]/form/div/div/div'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 50
def twentyFourHourScraper(driver, fileName):
    driver.get("https://24hour.email/mailbox/")  # Change to your target website
    xpath2 = '//*[@id="current-id"]'
    content = get_element_value_2(driver, xpath2)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 51
def suteScraper(driver, fileName):
    # Open the desired website
    driver.get("https://sute.jp/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div/span'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 52
def tenMinMailNetScraper(driver, fileName):
    driver.get("https://10minutemail.info/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="fe_text"]'

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content,fileName)
    return

# 54
def disposableScraper(driver, fileName):
    # Open the desired website
    driver.get("https://www.disposablemail.com/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 60
def snapMailScraper(driver, fileName):
    driver.get("https://snapmail.cc")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/div/div[2]/div[1]/ul[1]/li[2]/a/span[1]'
    time.sleep(1)
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 61
def tijDeliScraper(driver, fileName):
    driver.get("https://tijdelijke-email.nl/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '/html/body/header/div/h1'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 66
def trashSpamScraper(driver, fileName):
    driver.get("https://www.trashspam.com")  # Change to your target website
    button_xpath = '/html/body/div/div/div/div[3]'
    get_button_clicked(driver, button_xpath)
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    # # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 68
def tempeMailScraper(driver, fileName):
    driver.get("https://tempemails.net/")  # Change to your target website
    time.sleep(6) # for getting content
    # Get the HTML content of the page
    html_content = driver.page_source
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the content of <h1> tag inside <header> inside <main>
    main_content = soup.find('main')
    header_content = main_content.find('header') if main_content else None
    h1_content = header_content.find('h1') if header_content else None

    # Get the text content of the <h1> tag
    h1_text = h1_content.get_text(strip=True) if h1_content else ''
    # Save the retrieved content to a text file
    save_to_file(h1_text, fileName)
    return

# 69
def clipMailScraper(driver, fileName):
    driver.get("https://clipmails.com/")  # Change to your target website
    time.sleep(6) # for getting content
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    save_to_file(content, fileName)
    return

# 71 
def getInboxScraper(driver, fileName):
    driver.get("http://ww1.getinboxes.com/")  # Change to your target website
    time.sleep(3) # for getting content
    input_xpath = '/html/body/div/main/header/h1'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    save_to_file(content, fileName)
    return

# 79
def tempMailNinjaScraper(driver, fileName):
    driver.get("https://tempmail.ninja/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# 85
def mailHazardScraper(driver, fileName):
    driver.get("http://ww7.mailhazard.com")  # Change to your target website

    time.sleep(3) # for getting content
    input_xpath = '/html/body/div/main/header/h1'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    save_to_file(content, fileName)
    return

# 92
def mailTemporaireScraper(driver, fileName):
    driver.get("https://www.mail-temporaire.fr/")  # Change to your target website
    button_xpath = '/html/body/table/tbody/tr/td[2]/div/div[2]/form/div[1]/table/tbody/tr/td/b/a'
    get_button_clicked(driver, button_xpath)
    input_xpath = '//*[@id="searchinput"]'
    content = get_element_value_2(driver, input_xpath)
    content = filter_content(content)
    save_to_file(content, fileName)
    return

# 97
def tempSkyScraper(driver, fileName):
    driver.get("http://ww1.tempsky.com/lander")  # Change to your target website

    time.sleep(3) # for getting content
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    # Get the value from the specified element
    content = get_element_value(driver, input_xpath)
    content = filter_content(content)
    print(content)
    save_to_file(content, fileName)
    return

# 101
def tempMailIOScraper(driver, fileName):
    driver.get("https://tempmail.io/")  # Change to your target website

    # XPath for the element you want to retrieve
    input_xpath = '//*[@id="email"]'

    # Get the value from the specified element
    content = get_element_attribute(driver, input_xpath, "value")
    content = filter_content(content)
    print(content)
    # Save the retrieved content to a text file
    save_to_file(content, fileName)
    return

# Main execution
def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    outputFile = "staticDomains.txt"
    InboxKittenScraper(driver, outputFile)
    mailCatchScraper(driver, outputFile)
    minuteInboxScraper(driver, outputFile)
    fakeeMailScraper(driver, outputFile)
    harikiriMailScraper(driver, outputFile)
    uroidScraper(driver, outputFile)
    tenMinMailScraper(driver, outputFile) 
    eyePasteScraper(driver, outputFile)
    einWegScraper(driver, outputFile)
    mail1aScraper(driver, outputFile)
    suteScraper(driver, outputFile)
    tenMinMailNetScraper(driver, outputFile) 
    disposableScraper(driver, outputFile)
    snapMailScraper(driver, outputFile)
    tijDeliScraper(driver, outputFile)
    trashSpamScraper(driver, outputFile)
    tempeMailScraper(driver, outputFile)
    clipMailScraper(driver, outputFile)
    getInboxScraper(driver, outputFile)
    tempMailNinjaScraper(driver, outputFile)
    mailHazardScraper(driver, outputFile)
    mailTemporaireScraper(driver, outputFile)
    tempSkyScraper(driver, outputFile)
    tempMailIOScraper(driver, outputFile)
    tempailScraper(driver, outputFile) 
    tenMinMailScraper(driver, outputFile)
    yopMailScraper(driver, outputFile)
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
