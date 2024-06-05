from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def proMailNetScraper(driver):
    try:
        # Fetch the page content using the Selenium WebDriver
        page_source = driver.page_source

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Use CSS selectors to locate the specific section
        div = soup.select_one('body > div:nth-of-type(3) > section:nth-of-type(2) > div:nth-of-type(1) > div > div > div:nth-of-type(1) > div > div:nth-of-type(2) > div:nth-of-type(6) > span')

        if div:
            # Fetch all <a> tags within the specified section
            a_tags = div.find_all('a')

            # Extract the content (text) of each <a> tag
            a_texts = [a.get_text() for a in a_tags]

            return a_texts
        else:
            return []
    except Exception as e:
        print(f"Error processing the webpage: {e}")
        return []


def main():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the URL
        url = 'https://verifymail.io/domain/promail9.net'
        driver.get(url)

        # Call the proMailNetScraper function
        result = proMailNetScraper(driver)

        # Print the result
        print(result)
    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    main()
