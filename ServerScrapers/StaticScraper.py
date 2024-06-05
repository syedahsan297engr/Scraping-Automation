from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import argparse
from bs4 import BeautifulSoup
from utilities import get_element_value, get_element_value_2, get_element_attribute, save_to_csv, get_button_clicked, extract_inner_divs_content, save_list_to_csv

# 1
def tempMailScraper(driver, filePath):
    driver.get("https://temp-mail.org/en/")  
    input_xpath = "//input[@id='mail']"
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content,"temp-mail.org", filePath)
    return

# 6
def mailCatchScraper(driver, filePath):
    driver.get("http://mailcatch.com")  
    email_xpath = "//*[@id='copy-button']"
    content = get_element_attribute(driver, email_xpath, "data-clipboard-text")
    save_to_csv(content, "mailcatch.com", filePath)
    return

# 10
def tenMinMailScraper(driver, filePath):
    driver.get("https://10minutemail.net/")  
    input_xpath = '//*[@id="fe_text"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "10minutemail.net", filePath)
    return

# 11
def minuteInboxScraper(driver, filePath):
    driver.get("https://www.minuteinbox.com/")  
    input_xpath = '//*[@id="email"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "minuteinbox.com", filePath)
    return

# 12
def InboxKittenScraper(driver, filePath):
    driver.get("https://inboxkitten.com/")  
    input_xpath = '//*[@id="div-domain"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "inboxkitten.com", filePath)
    return

# 13
def tempailScraper(driver, filePath):
    driver.get("https://tempail.com/")  
    input_xpath = '//*[@id="eposta_adres"]' # //*[@id="eposta_adres"]
    content = get_element_value_2(driver, input_xpath)
    save_to_csv(content, "tempail.com", filePath)
    return


# beautiful soup used for this
# 14
def yopMailScraper(driver, filePath):
    driver.get("https://yopmail.com/alternate-domains")
    # XPath for the iframe containing the div with class 'lstdom'
    iframe_xpath = '//*[@id="ifdoms"]'
    # Extract inner div contents from the iframe
    inner_divs_content = extract_inner_divs_content(driver, iframe_xpath)
    # Save the content to a text file
    save_list_to_csv(inner_divs_content,"yopmail.com", filePath)

    # Close the WebDriver
    driver.quit()
    return

# 31
def fakeeMailScraper(driver, filePath):
    driver.get("https://fakeemail.co/")  
    input_xpath = '/html/body/div/div/header/div/div/div/div[2]/div/div[2]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "fakeemail.co", filePath)
    return

# 32
def harikiriMailScraper(driver, filePath):
    driver.get("https://harakirimail.com/")  
    input_xpath = '//*[@id="randominboxLink"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "harakirimail.com", filePath)
    return

# 34
def uroidScraper(driver, filePath):
    driver.get("https://uroid.com/")  
    input_xpath = '//*[@id="eposta_adres"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "uroid.com", filePath)
    return


# 43
def eyePasteScraper(driver, filePath):
    driver.get("https://www.eyepaste.com/")  
    input_xpath = '/html/body/div[1]/div[2]/div/h1'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "eyepaste.com", filePath)
    return


# 46
def einWegScraper(driver, filePath):
    driver.get("https://www.einweg-email.com")  
    input_xpath = '//*[@id="my-address"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "einweg-email.com", filePath)
    return

# 47
def mail1aScraper(driver, filePath):
    driver.get("https://mail1a.de/")  
    input_xpath = '/html/body/div[2]/div[1]/div[1]/form/div/div/div'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "mail1a.de",  filePath)
    return

# 50
def twentyFourHourScraper(driver, filePath):
    driver.get("https://24hour.email/mailbox/")  
    xpath2 = '//*[@id="current-id"]'
    content = get_element_value_2(driver, xpath2)
    save_to_csv(content, "24hour.email/mailbox", filePath)
    return

# 51
def suteScraper(driver, filePath):
    driver.get("https://sute.jp/")  
    input_xpath = '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div/span'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "sute.jp", filePath)
    return

# 52
def tenMinMailNetScraper(driver, filePath):
    driver.get("https://10minutemail.info/")  
    input_xpath = '//*[@id="fe_text"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "10minutemail.info", filePath)
    return

# 54
def disposableScraper(driver, filePath):
    driver.get("https://www.disposablemail.com/")  
    input_xpath = '//*[@id="email"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "disposablemail.com", filePath)
    return

# 60
def snapMailScraper(driver, filePath):
    driver.get("https://snapmail.cc")  
    # /html/body/div/div[1]/div[2]/div[2]/ul/li/a/span/span
    input_xpath = '/html/body/div/div[2]/div[1]/ul[1]/li[2]/a/span[1]'
    time.sleep(1)
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "snapmail.cc", filePath)
    return

# 61
def tijDeliScraper(driver, filePath):
    driver.get("https://tijdelijke-email.nl/")  
    input_xpath = '/html/body/header/div/h1'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "tijdelijke-email.nl", filePath)
    return

# 66
def trashSpamScraper(driver, filePath):
    driver.get("https://www.trashspam.com")  
    button_xpath = '/html/body/div/div/div/div[3]'
    get_button_clicked(driver, button_xpath)
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "trashspam.com", filePath)
    return

# 68
def tempeMailScraper(driver, filePath):
    driver.get("https://tempemails.net/")  
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
    save_to_csv(h1_text, "tempemails.net", filePath)
    return

# 69
def clipMailScraper(driver, filePath):
    driver.get("https://clipmails.com/")  
    time.sleep(6) # for getting content
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "clipmails.com", filePath)
    return

# 71 
def getInboxScraper(driver, filePath):
    driver.get("http://ww1.getinboxes.com/")  
    time.sleep(3) # for getting content
    input_xpath = '/html/body/div/main/header/h1'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "getinboxes.com",  filePath)
    return

# 79
def tempMailNinjaScraper(driver, filePath):
    driver.get("https://tempmail.ninja/")  
    input_xpath = '//*[@id="email"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "tempmail.ninja",  filePath)
    return


# 92
def mailTemporaireScraper(driver, filePath):
    driver.get("https://www.mail-temporaire.fr/")  
    button_xpath = '/html/body/table/tbody/tr/td[2]/div/div[2]/form/div[1]/table/tbody/tr/td/b/a'
    get_button_clicked(driver, button_xpath)
    input_xpath = '//*[@id="searchinput"]'
    content = get_element_value_2(driver, input_xpath)
    save_to_csv(content, "mail-temporaire.fr", filePath)
    return

# 97
def tempSkyScraper(driver, filePath):
    driver.get("http://ww1.tempsky.com/lander")  
    time.sleep(3) # for getting content
    input_xpath = '/html/body/div/div/div/div[1]/div[2]/div'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "empsky.com",  filePath)
    return

# 101
def tempMailIOScraper(driver, filePath):
    driver.get("https://tempmail.io/")  
    input_xpath = '//*[@id="email"]'
    content = get_element_attribute(driver, input_xpath, "value")
    save_to_csv(content, "tempmail.io",  filePath)
    return
# 56
def fakeMailScraper(driver, filePath):
    driver.get("https://www.fakemail.net/")
    input_xpath = '//*[@id="email"]'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "fakemail.net", filePath)
    return

# 37
def anonBoxScraper(driver, filePath):
    driver.get("https://anonbox.net/en/")
    input_xpath = '/html/body/div[2]/dl/dd[2]/p'
    content = get_element_value(driver, input_xpath)
    save_to_csv(content, "anonbox.net", filePath)
    return


#//*[@id="file-free_email_provider_domains-txt-LC3"]
def freeEmailProvidersGitHubScraper(driver, filePath):
    driver.get("https://gist.github.com/mpyw/6b59ffbe517da9cccbf40db9aa30d09b")  
    domains = []
    # total 9683 records are there on github
    for id in range (1, 9683):
        xpath = f'//*[@id="file-free_email_provider_domains-txt-LC{id}"]'
        currDomain = get_element_value(driver, xpath)
        domains.append(currDomain)
    # print(len(domains)) #5886 #20815
    save_list_to_csv(domains, "github.mpyw", filePath)
    return

def parse_arguments():
    parser = argparse.ArgumentParser(description='InboxKitten Scraper')
    parser.add_argument('outputFilePath', type=str, help='Path to the output CSV file')
    return parser.parse_args()

# Main execution
def main():
    args = parse_arguments()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    outputFilePath = args.outputFilePath
    # InboxKittenScraper(driver, outputFilePath)
    # mailCatchScraper(driver, outputFilePath)
    # minuteInboxScraper(driver, outputFilePath)
    # fakeeMailScraper(driver, outputFilePath)
    # harikiriMailScraper(driver, outputFilePath)
    # uroidScraper(driver, outputFilePath)
    # eyePasteScraper(driver, outputFilePath)
    # einWegScraper(driver, outputFilePath)
    # mail1aScraper(driver, outputFilePath)
    # suteScraper(driver, outputFilePath)
    # tenMinMailNetScraper(driver, outputFilePath) 
    # disposableScraper(driver, outputFilePath)
    # snapMailScraper(driver, outputFilePath) 
    # tijDeliScraper(driver, outputFilePath)
    # trashSpamScraper(driver, outputFilePath)
    # tempeMailScraper(driver, outputFilePath)
    # clipMailScraper(driver, outputFilePath)
    # getInboxScraper(driver, outputFilePath)
    # tempMailNinjaScraper(driver, outputFilePath) 
    # mailTemporaireScraper(driver, outputFilePath)
    # tempSkyScraper(driver, outputFilePath)
    # tempMailIOScraper(driver, outputFilePath)
    # anonBoxScraper(driver, outputFilePath)
    # fakeeMailScraper(driver, outputFilePath)
    # # freeEmailProvidersGitHubScraper(driver, outputFilePath)
    tenMinMailScraper(driver, outputFilePath)
    tempailScraper(driver, outputFilePath) 
    # yopMailScraper(driver, outputFilePath)
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
