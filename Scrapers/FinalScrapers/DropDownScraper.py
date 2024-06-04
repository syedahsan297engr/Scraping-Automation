from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from utilities import handle_form, get_button_clicked, get_drop_down, save_list_to_csv, save_list_to_csv_old

    
# 4
def guerillaScraper(driver, filePath):
    driver.get("https://www.guerrillamail.com/")  
    dropdown_xpath = '//*[@id="gm-host-select"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "guerrillamail.com", filePath)
    return

# 3
def inboxesScraper(driver, filePath):
    driver.get("https://getnada.com")  
    button_selector = "/html/body/div[1]/main/div/div/div/div[1]/button"
    get_button_clicked(driver, button_selector)
    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[1]/main/div/div/div/div[1]/div[2]/div/div/div/form/div/div[2]/select"
    dropdown = handle_form(driver, dropdown_selector)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options[1:]]
    save_list_to_csv(dropdown_texts, "getnada.com", filePath)
    return

# 17
def temprMailScraper(driver, filePath):
    driver.get("https://tempr.email/")  
    dropdown_xpath = '//*[@id="LoginDomainId"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "tempr.email", filePath)
    return

# 19
def emailFakeScraper(driver, filePath):
    driver.get("https://emailfake.com/")  
    button_selector = "/html/body/div[3]/div/div/div/div[3]"
    get_button_clicked(driver, button_selector)
    # Locate the dropdown and extract its options (replace the selector with the correct one)
    dropdown_selector = "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div"
    dropdown = handle_form(driver, dropdown_selector)
    # Get all the option elements from the dropdown
    options = dropdown.find_elements(By.TAG_NAME, "p")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "emailfake.com", filePath)
    return

# 20
def generatorMailScraper(driver, filePath):
    driver.get("https://generator.email/")  
    button_selector = "/html/body/div[3]/div/div/div/div[3]"
    get_button_clicked(driver, button_selector)
    dropdown_selector = "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "p")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "generator.email",  filePath)
    return

# 21
def temporaryMailNetScraper(driver, filePath):
    driver.get("https://www.fakemailgenerator.net/")  
    button_selector = "/html/body/section[1]/div/div/div[2]/div/div[2]/button"
    get_button_clicked(driver, button_selector)
    dropdown_selector = "/html/body/section[1]/div/div/div[2]/div/div[2]/ul"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options[1:]]
    save_list_to_csv(dropdown_texts, "fakemailgenerator.net", filePath)
    return

# 22
def fakeMailGeneratorScraper(driver, filePath):
    driver.get("http://www.fakemailgenerator.com")  
    button_selector = '/html/body/div[1]/div[1]/div[1]/div[1]/div/div/button'
    get_button_clicked(driver, button_selector)
    dropdown_selector = "/html/body/div[1]/div[1]/div[1]/div[1]/div/div/ul/li"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options] 
    save_list_to_csv(dropdown_texts, "fakemailgenerator.com", filePath)
    return

# 23
def mailFakeScraper(driver, filePath):
    driver.get("https://mail-fake.com/")  
    button_selector = "/html/body/div[3]/div/div/div/div[3]"
    get_button_clicked(driver, button_selector)
    dropdown_selector = "/html/body/div[3]/div/div/div/div[2]/div[2]/div/div"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "p")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "mail-fake.com", filePath)
    return

# 24
def fakeTempMailScraper(driver, filePath):
    driver.get("https://faketempmail.com/")  
    button_selector = "/html/body/div/div/div[1]/div[3]/div/div/div/div/div/div/aside[1]/ul/li[1]/div/button[1]"
    get_button_clicked(driver, button_selector)
    dropdown_selector = "/html/body/div/div/div[1]/div[3]/div/div/div/div/div/div/aside[1]/ul/li[1]/div/ul"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "span")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "faketempmail.com", filePath)
    return

# 25
def instantMailScraper(driver, filePath):
    driver.get("https://instant-email.org/")  
    dropdown_xpath = '//*[@id="domain"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "instant-email.org", filePath)
    return

# 29
def mailGenScraper(driver, filePath):
    driver.get("https://mailgen.biz/")  
    dropdown_xpath = '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/form[1]/div/div/div[1]/div[1]/input'
    get_button_clicked(driver, dropdown_xpath)
    dropdown_selector = "/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/form[1]/div/div/div[1]/div[2]/div"
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "mailgen.biz", filePath)
    return

# 30
def trashMailScraper(driver, filePath):
    driver.get("https://www.trash-mail.com/new-address/")  
    dropdown_xpath = '//*[@id="form-domain-new-id"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]   
    save_list_to_csv(dropdown_texts, "trash-mail.com", filePath)
    return

# 36
def lorteMailScraper(driver, filePath):
    driver.get("https://lortemail.dk/")  
    dropdown_xpath = '/html/body/section[1]/div/div[2]/div[2]/form/fieldset/div[2]/div/select'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "lortemail.dk", filePath)
    return

# 38
def oneSecMailScraper(driver, filePath):
    driver.get("https://www.1secmail.com/")  
    dropdown_xpath = '/html/body/div/div[4]/div[1]/form/div/select'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "1secmail.com", filePath)
    return

# 39
def mailTempGmailScraper(driver, filePath):
    driver.get("https://mail-temp.com/blog/temp-gmail-generator#google_vignette")  
    button_selector = '//*[@id="drop_sel"]'
    get_button_clicked(driver, button_selector)
    dropdown_selector = '//*[@id="newselect"]'
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "p")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "mail-temp.com", filePath)
    return

# 40
def trashMailScraper(driver, filePath):
    driver.get("https://trashmail.com/")  
    dropdown_xpath = '//*[@id="fe-mob-domain"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "trashmail.com", filePath)
    return

# 42
def moaktScraper(driver, filePath):
    driver.get("https://www.moakt.com/fr")  
    dropdown_xpath = '/html/body/div[1]/div/div[2]/div/div/form/span[2]/span/select/optgroup'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "moakt.com", filePath)
    return

# 44
def muellMailScraper(driver, filePath):
    driver.get("https://muellmail.com/en#google_vignette")  
    dropdown_xpath = '/html/body/div[2]/main/div[2]/div[2]/div[2]/div/div/div[1]/select'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "muellmail.com", filePath)
    return

# 49
def dropMailScraper(driver, filePath):
    driver.get("https://dropmail.me")  
    button_selector = '/html/body/div[2]/div[4]/div[1]/button[2]'
    get_button_clicked(driver, button_selector)
    dropdown_selector = '//*[@id="dropdown"]'
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "a")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "dropmail.me", filePath)
    return

# 57
def mailTempScraper(driver, filePath):
    driver.get("https://mail-temp.com")  
    button_selector = '/html/body/div[2]/div/div/div[2]/div/div/div[3]'
    get_button_clicked(driver, button_selector)
    dropdown_selector = '//*[@id="newselect"]'
    dropdown = handle_form(driver, dropdown_selector)
    options = dropdown.find_elements(By.TAG_NAME, "p")
    dropdown_texts = [option.text for option in options]
    save_list_to_csv(dropdown_texts, "mail-temp.com", filePath)
    return

# 58
def tempeMailScraper(driver, filePath):
    driver.get("https://tempemail.co/")  
    dropdown_xpath = '//*[@id="email_domain"]'
    dropdown = get_drop_down(driver, dropdown_xpath)
    options = dropdown.find_elements(By.TAG_NAME, "option")
    dropdown_texts = [option.text for option in options[1:]]
    save_list_to_csv(dropdown_texts, "tempemail.co", filePath)
    return

# Main execution logic
def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # no need to chromedriver_path
    outputFilePath = "/home/ahsan/Desktop/Scraping-Automation/Documents/disposable-domains.csv"
    guerillaScraper(driver, outputFilePath) 
    temprMailScraper(driver, outputFilePath) 
    emailFakeScraper(driver, outputFilePath)
    generatorMailScraper(driver, outputFilePath)
    temporaryMailNetScraper(driver, outputFilePath)
    fakeTempMailScraper(driver, outputFilePath)
    instantMailScraper(driver, outputFilePath)
    trashMailScraper(driver, outputFilePath)
    lorteMailScraper(driver, outputFilePath)
    oneSecMailScraper(driver, outputFilePath)
    mailTempGmailScraper(driver, outputFilePath) 
    trashMailScraper(driver, outputFilePath)
    moaktScraper(driver, outputFilePath) 
    muellMailScraper(driver, outputFilePath) 
    dropMailScraper(driver, outputFilePath) 
    mailTempScraper(driver, outputFilePath) 
    tempeMailScraper(driver, outputFilePath) 
    mailFakeScraper(driver, outputFilePath) 
    inboxesScraper(driver, outputFilePath) # takes more time to scrap 
    fakeMailGeneratorScraper(driver, outputFilePath) # takes time
    mailGenScraper(driver, outputFilePath)
    # Close the WebDriver
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()
