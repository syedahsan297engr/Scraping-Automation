import json
from datetime import datetime, timedelta
import os
import shutil
import random
from time import sleep
import pyperclip
import psutil

from selenium import webdriver
# import undetected_chromedriver as uc
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

def close_chrome():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.info
            if 'chrome' in process_info['name'].lower():
                pid = process_info['pid']
                chrome_process = psutil.Process(pid)
                chrome_process.terminate()
                print(f"Terminated Chrome process with PID {pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def delay(min, max):
    n = random.randrange(min*100,max*100)
    n = n/100
    print(f"***Delay Time! Waiting {n} seconds***")
    sleep(n)

def get_data(data):
    with open(data, 'r') as file:
        json_data = json.load(file)
    times = [json_data[0]['time{}'.format(i)] for i in range(1, json_data[0]['videos'] + 1)]
    days = json_data[0]["nbday"]
    videos = json_data[0]["videos"]
    date = json_data[0]["startdate"]
    return times, days, videos, date

def find_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Initialize variables to store the paths
    youtube_api_file = None
    image_file = None
    video_file = None
    
    # Get the folder name
    folder_name = os.path.basename(folder_path)
    
    # Search for files matching the criteria
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        if file_ext == '.json' and 'en_youtube_api' in file_name:
            youtube_api_file = os.path.abspath(os.path.join(folder_path, file))
        elif file_ext in ['.jpg', '.jpeg', '.png'] and folder_name == file_name:
            image_file = os.path.abspath(os.path.join(folder_path, file))
        elif file_ext in ['.mp4', '.avi', '.mov'] and folder_name in file_name  and "en_youtube" in file_name:
            video_file = os.path.abspath(os.path.join(folder_path, file))
    
    return youtube_api_file, image_file, video_file

def extract_title_description(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    if not data or 'title' not in data[0] or 'description' not in data[0]:
        return None, None
    
    title = data[0]['title']
    description = data[0]['description']
    
    return title, description

def move_folder_to_done(folder_path, done_folder_path):
    if not os.path.exists(done_folder_path):
        os.makedirs(done_folder_path)
    
    folder_name = os.path.basename(folder_path)
    new_folder_path = os.path.join(done_folder_path, folder_name)
    
    shutil.move(folder_path, new_folder_path)
    print(f"Folder '{folder_name}' moved to '{done_folder_path}'.")

def store_target_datetime(target_hour, target_date):
    # Create or replace the file
    with open("history.txt", "w") as file:
        # Write the target time and date to the file
        file.write(f"Time: {target_hour}\n")
        file.write(f"Date: {target_date}\n")

def YT_upload(video, image_file, V_TITLE, V_DESCRIPTION, timeF, dateF): 
    PATH = r"chromedriver.exe"
    opt = webdriver.ChromeOptions()
    opt.add_argument(f"user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\")
    # opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    # opt.add_experimental_option("detach", True)
    driver =  webdriver.Chrome(options=opt)
    delay(2,4)
    driver.get("https://youtube.com\\upload")
    driver.maximize_window()
    delay(2,4)
    driver.get("https://youtube.com\\upload")

        
    i1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@type='file']")))
    delay(3,6)
    i1.send_keys(video)
    print("UPLOADING VIDEO")
    
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "textbox")))
    delay(2,4)
    pyautogui.hotkey('tab')
    i1 = driver.find_elements(By.ID, 'textbox')
    print("FOUND TESTBOX")

    while(True):
        i1[0].clear()
        i1[0].send_keys(V_TITLE)
        text = i1[0].get_attribute("textContent")
        if len(text) == len(V_TITLE):
            print("Title is correct")
            break
    print("ENTERED TITLE OF VIDEO")

    delay(1,3)
    #i1[1].clear()
    i1[1].send_keys(Keys.HOME + V_DESCRIPTION + "\n")
    delay(1,3)
    print("ENTERED DESCRIPTION OF VIDEO")
    
    print("WAITING FOR UPLOAD COMPLETE")
    i1 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "progress-label")))
    counter = 0
    while True:
        if i1.text == "Uploading 100% ..." or i1.text[0:15] == "Upload complete" or i1.text[0:8] == "Checking" or i1.text == "Checks complete. No issues found." or i1.text[0:10] == "Processing" or i1.text == "" or i1.text[0:15] == "Checks complete":
            print("Uploaded", counter)
            break
        else:
            sleep(0.5)
            counter -= -1
        
        if counter >= 360:
            print("Timeout")
            break

    print("upload at 100%")
    delay(2,4)

    # SELECT THUMBNAIL(NEEDS VERIFIED PHONE NUMBER)
    base_path = os.path.dirname(image_file)
    file_name = os.path.basename(image_file)
    print("Base path:", base_path)
    print("File name:", file_name)
    sb = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "select-button")))
    sb.click()
    
    delay(2,3)
    print("ctrl+L")
    pyautogui.hotkey('ctrl', 'l')
    delay(1,2)
    print("WRITING ADDRESS")
    pyperclip.copy(base_path)
    print("ctrl+v")
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.typewrite(base_path, interval=0.1)
    delay(1,2)
    print("enter")
    pyautogui.hotkey('enter')
    delay(1,2)

    print("tab")
    pyautogui.hotkey('tab')
    delay(0.5,1)
    print("tab")
    pyautogui.hotkey('tab')
    delay(0.5,1)
    print("tab")
    pyautogui.hotkey('tab')
    delay(0.5,1)
    print("tab")
    pyautogui.hotkey('tab')
    delay(0.5,1)
    print("tab")
    pyautogui.hotkey('tab')
    delay(0.5,1)
    pyperclip.copy(file_name)
    print("ctrl+v")
    pyautogui.hotkey('ctrl', 'v')
    delay(1,2)
    print("enter")
    pyautogui.hotkey('enter')
    
    delay(3,6)
        
    print("SEARCHING FOR RADIO BUTTON")
    try:
        button = driver.find_element(By.XPATH, "//tp-yt-paper-radio-button[@name='VIDEO_MADE_FOR_KIDS_NOT_MFK']")
        delay(2,4)
        button.click()
        print("Radio Button clicked")
    except Exception as E9:
        print("radio button kids content not found/error")
        print(E9)

    delay(2,4)
    # driver.implicitly_wait(10)

    i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "next-button")))
    i1.click()
    print("clicked next button 1")
    delay(1,2)

    i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "next-button")))
    i1.click()
    print("clicked next button 2")
    delay(1,2)

    i1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "next-button")))
    i1.click()
    print("clicked next button 3")
    delay(2,4)

    # sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "radioLabel")))
    i1 = driver.find_elements(By.ID, 'radioLabel')

    delay(3,5)
    i1[2].click()
    print("Radio Button clicked")
    
    delay(1,2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "second-container-expand-button")))
    ia = driver.find_element(By.ID, 'second-container-expand-button')
    ia.click()
    
    delay(3,5)
    ib = driver.find_element(By.ID, 'datepicker-trigger')
    ib.click()


    delay(2,3)
    #pyautogui.hotkey('tab')
    #sleep(0.5)
    #pyautogui.hotkey('tab')
    #sleep(0.5)
    

    # optional
    # parsed_date = datetime.strptime(dateF, "%b %d, %Y")
    # dateF = parsed_date.strftime("%d %b %Y")
    
    while(True):
        divs = driver.find_elements(By.CLASS_NAME, "calendar-month.style-scope.ytcp-scrollable-calendar")
        month_index = -69
        delay(0.7,1.5)
        # sleep(0.5)
        for index, div in enumerate(divs):
            first_div = div.find_element(By.XPATH, ".//div[1]")
            text = first_div.text
            # print(dateF.split(' ')[0].lower())
            # print(text)
            try:
                year = text.split(' ')[1].lower()
                # print(year)
            except:
                continue
            if text.split(" ")[0].lower()[0:3] == dateF.split(' ')[0].lower()[0:3] and int(year) == int(dateF.rsplit(" ")[-1]):
                print("Index of matching div:", index)
                month_index = index
                break
        if month_index == -69:
            NEXT = driver.find_element(By.ID, "next-month")
            NEXT.click()
        else:
            break
            
    day = int(dateF.split(" ")[1].split(",")[0])
    # print(day)
    month = divs[month_index]

    spans = month.find_elements(By.XPATH, ".//div[position() > 1]//span")
    for span in spans:
        span_text = span.text
        try:
            span_number = int(span_text)
        except ValueError:
            continue
        # print(span_number)
        if span_number == day:
            print(span_number)
            span.click()
            break
        
    delay(4,6)

    # Optional script to convert 08:00PM to this format 20:00
    # parsed_time = datetime.strptime(timeF, "%I:%M%p")
    # timeF = parsed_time.strftime("%H:%M")
        
    ie = driver.find_element(By.CLASS_NAME, 'style-scope tp-yt-paper-input')
    ie.send_keys(Keys.CONTROL + "a")
    ie.send_keys(timeF)
    # Release the Control key
    ie.send_keys(Keys.CONTROL + Keys.NULL)
    delay(2,4)

    # SCRAPPED TAB WORK CAUSING ISSUES
    # pyperclip.copy(dateF)
    # print("ctrl+a")
    # pyautogui.hotkey('ctrl', 'a')
    # sleep(1)
    # print("ctrl+v")
    # pyautogui.hotkey('ctrl', 'v')
    # sleep(1)
    # pyautogui.hotkey('enter')


    print("Waiting for done-button")
    i1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "done-button")))
    delay(5,10)
    i1.click()
    print("Done-Button clicked")

    delay(3,6)

    counter = 0
    while True:
        if "Video scheduled" in driver.page_source or "Uploaded" in driver.page_source or "Video published" in driver.page_source:
            break
        else:
            sleep(0.5)
            counter -= -1
        
        if counter >= 600:
            print("Timeout")
            break
        
    print("VIDEO UPLOAD FUNCTION DONE SUCCESSFULLY")
    delay(5,12)
    driver.quit()
    
def check_json():
    with open("data.json", 'r') as file:
        json_data = json.load(file)
    try:
        times = [json_data[0]['time{}'.format(i)] for i in range(1, json_data[0]['videos'] + 1)]
        return True
    except:
        print("Times are less then videos in data.json")
        return False

def convert_to_12_hour_format(hour):
    if hour >= 24:
        hour = 0
    dt = datetime.strptime(str(hour), "%H")
    # Convert to 12-hour format with AM or PM
    return dt.strftime("%I:%M%p")

def convert_date_format(date_str):
    dt = datetime.strptime(date_str, "%d/%m/%Y")
    # Format the date as "Month day, year"
    formatted_date = dt.strftime("%b %d, %Y")
    return formatted_date

def check_date_match(target_hour, target_date):
    target_dt = datetime.strptime(target_date + " " + target_hour, "%b %d, %Y %I:%M%p")
    current_dt = datetime.now()
    if target_dt > current_dt:
        return True
    else:
        return False

def mainloops():
    
    close_chrome()
    
    # PATH = r"chromedriver.exe"
    # opt = webdriver.ChromeOptions()
    # opt.add_argument(f"user-data-dir=C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\")
    # # opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    # # opt.add_experimental_option("detach", True)
    # driver =  webdriver.Chrome(options=opt)
    # delay(3,5)
    # driver.quit()
    
    input_folder_path = r'YT'
    try:
        folders = [f for f in os.listdir(input_folder_path) if os.path.isdir(os.path.join(input_folder_path, f)) and f != 'done']
    except Exception as e0:
        print(f"Error {e0}")
        print("No YT Folder found. Please check and correct it")
        return
    print(f"Found {len(folders)} YouTube folders")
    
    if (len(folders)) == 0:
        print(f"No Folders found please make sure video folders are present in YT folder")
        return
    
    if check_json():
        pass
    else:
        return
    
    for index, x in enumerate(folders):
        print(f"Folder {index+1}: {x}")
        
    times, days, videos, date = get_data('data.json') # 17/02/2024 ---> Feb 17, 2024
    print("Times:", times)
    print("Days:", days)
    print("Videos:", videos)
    print("\n")
    
    date_str = convert_date_format(date)
    date_format = "%b %d, %Y"
    current_date = datetime.strptime(date_str, date_format)

    input_folder_path = r'YT'
    for day in range(days):
        target_date = current_date.strftime(date_format) 
        
        print(f"*** DAY: {day+1}/{days} ***")
        folders = [f for f in os.listdir(input_folder_path) if os.path.isdir(os.path.join(input_folder_path, f)) and f != 'done']
        if len(folders) == 0:
            print("ALL UPLOADED, NO MORE FOLDERS, QUITTING")
            break
        else:
            print(f"{len(folders)} Video Folders available in YT Folder. Proceeding")
            
            
        # Select X random folders without duplicates
        selected_folders = random.sample(folders, min(videos, len(folders)))
        print("Working on Selected folders")
        for video_num, folder in enumerate(selected_folders):
            try:
                print(f"*** Current Folder: {folder} ***")
                hour = times[video_num] ############################################ SCHEDULER TIME
                target_hour = convert_to_12_hour_format(hour)
                print("Current Time:", datetime.now().strftime('%H:%M:%S'))
                
                # print("Current Time is:", datetime.now().strftime('%H:%M:%S'))
                print(f"*** {video_num+1} --> Selected Folder for Upload: {folder} ***")
                folder_path = os.path.join("YT", folder)
                youtube_api_file, image_file, video_file = find_files(folder_path)

                # Print or save the paths
                if youtube_api_file:
                    print("YouTube API JSON file found: ", youtube_api_file)
                    title, description = extract_title_description(youtube_api_file)
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                else:
                    print(f"No youtube_api_file found\nContinuing to Next Folder")
                    continue

                if image_file:
                    print("Image file found:", image_file)
                else:
                    print(f"No Image found\nContinuing to Next Folder")
                    continue
                if video_file:
                    print("Video file found:", video_file)
                else:
                    print(f"No Video found\nContinuing to Next Folder")
                    continue
                    
                print(f"Schedule Time: {target_hour}")
                print(f"Schedule Date: {target_date}")

                go = check_date_match(target_hour, target_date) 
                if go:
                    pass
                else:
                    print("********* Schedule Date and Time had passed so Skipping this Upload**********\n")
                    continue

                YT_upload(video_file, image_file, title, description, target_hour, target_date)
                
                os.makedirs("done", exist_ok=True)
                move_folder_to_done(folder_path, "done")
                print("\n")
                store_target_datetime(target_hour, target_date)
                sleep(7)
                #return
            except Exception as e000:
                print(e000)
                print(f"Error in YT Upload, continuing to next video")
                delay(3,5)
                close_chrome()
                try:
                    os.makedirs("Error Videos", exist_ok=True)
                    move_folder_to_done(folder_path, "Error Videos")
                except Exception as e09:
                    print(e09)
                    print("Couldnt move to error folder")
                delay(3,7)
                continue
                
        current_date += timedelta(days=1)

mainloops()
alpha = str(input("Press any key to exit"))
print("Quitting")