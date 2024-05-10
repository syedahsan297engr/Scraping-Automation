from bs4 import *
import requests
import os

from selenium import webdriver
import undetected_chromedriver as uc

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

from time import sleep

# Make sure to download chromedriver

# Opening a Webpage
def open_web():
    global driver
    PATH = f"C:\\Users\\{os.getlogin()}\\\Documents\\chromedriver.exe"
    opt = webdriver.ChromeOptions()
    opt.add_argument(f"user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\") #path of chromedriver
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_experimental_option("detach", True)
    # driver.headless = True # open browser hidden
    driver =  webdriver.Chrome(executable_path=PATH, options=opt)
    driver.maximize_window()
    driver.get("https://google.com") #enter your website here
    # driver.quit() #this will close the browser

# Important Functions

# Wait until presence of element located
i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@type='file']")))
i1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "progress-label")))
i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "next-button")))
i1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"][accept="image/bmp,image/gif,image/jpeg,image/png,image/tiff,image/webp,video/mp4,video/x-m4v,video/quicktime"]')))
 

# Wait until element is clickable
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-y1m958")))
 

# Finding element or multiple elements
i1 = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
i1 = driver.find_elements(By.ID, 'textbox')

#Something iframe which blocks elements, so here we are switching to it to find elements
#This was encountered while automating TikTok
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe')
driver.switch_to.frame(iframe)

# Wait until a button is cickable
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-y1m958")))
i1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "done-button")))


# Clearing and entering text in a textbox
#considering i1 is a variable assigned to a textbox
i1.clear()
i1.send_keys("text")

# To print text of an element
i1.text
    
# XPATH
#This method can be used to find any element
#This is a complex method which i still havent worked on much
#It requires exact path of element inside HTML
publish_button = driver.find_element(By.XPATH, '//*[@data-test-id="board-dropdown-save-button"]')

# To check if some text is present on a webpage
if "this text" in driver.page_source:
    pass


wait = WebDriverWait(driver, 10)

#Clicking buttons by button name
i4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Done')]"))) # here 'Done' is the text of that button
i4.click()
#clicking based on 1st few characters 
i7 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[starts-with(., 'Generate')]"))) # here button text was Generate (1) but the 1 could change

# Automating webpage in chrome using pyautoGUI

def auto_gui():
    pyautogui.hotkey('ctrl', 'f') #this open searchbox
    sleep(1)
    pyautogui.typewrite("Next", interval=0) #search for element to be clicked or element close to it
    sleep(1)
    pyautogui.hotkey('enter')
    sleep(1)
    pyautogui.hotkey('esc') #closing searchbox
    sleep(1)
    pyautogui.hotkey('tab') #tab to select it and press enter to click on it
    #incase a nearby element is selected, pressing tab multiple times can movoe cursor around the screen on next elements



response = requests.get(link, stream=True, timeout=7)
response.raise_for_status()  # Raise exception for non-200 status codes

# image_extension = link.split('.')[-1]
# image_filename = f'image_{idx + 1}.{image_extension}'
# image_path = os.path.join(subfolder_path, image_filename)
image_path = "C:\\image.png"

with open(image_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            
            
# Get classes out of a parent class
parent_class = "lister-list"
i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, parent_class)))

child_class = "lister-item-header"
y = i1.find_elements(By.CLASS_NAME, child_class)[2]
print(y.text)
y.click()