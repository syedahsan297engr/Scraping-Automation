import os
import csv
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Function to get a specific element's value using XPath
def get_element_value(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

def get_element_value_2(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.get_attribute("value")

# Function to get content from a specified attribute
def get_element_attribute(driver, xpath, attribute, timeout=10):
    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # Get the specified attribute from the element
    return element.get_attribute(attribute)


'''''''''Specific for Drop Down Scrapers'''''''''

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

'''''''''Specific for Drop Down Scrapers'''''''''



'''''''''Specific for Static Scrapers'''''''''

def get_button_clicked_2(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
    return

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

'''''''''Specific for Static Scrapers'''''''''

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

def save_to_csv(content, source, file_path):
    current_date = datetime.now().strftime('%Y-%m-%d')
    domain = filter_content(content)
    
    # Read existing entries from the CSV file to check for duplicates
    existing_entries = set()
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                existing_entries.add(row[0])

    # Check if the domain is already in the CSV file
    if domain not in existing_entries and len(domain) > 0:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([domain, source, current_date])
        print(f"Content successfully appended to {file_path}")
    else:
        if domain in existing_entries:
            updated = False
            updated_lines = []
            # Read the existing file content
            with open(file_path, 'r') as file:
                lines = file.readlines()
            # Process each line
            for line in lines:
                row = line.strip().split(',')
                if row[0] == domain:
                    # Ensure row has enough elements
                    while len(row) < 2:
                        row.append('')
                    # Update the row with new source and current date if source differs
                    if row[1] != source:
                        row[1] = source
                        row[2] = current_date
                        updated = True
                    line = ','.join(row) + '\n'
                updated_lines.append(line)
            # Write all lines back to the file
            with open(file_path, 'w', newline='') as file:
                file.writelines(updated_lines)
            if updated:
                print(f"Content '{domain}' updated with new source and date in {file_path}")
            else:
                print(f"Content '{domain}' already exists in {file_path}, but source differs")



def save_list_to_csv_old(contents, source, file_path):
    current_date = datetime.now().strftime('%Y-%m-%d')
    contents = filter_content(contents)
    # Read existing entries from the CSV file to check for duplicates
    existing_entries = set()
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                existing_entries.add(row[0])


    excluded_entries = {"INACTIVE SOON:", "Random domain", "INACTIVE SOON", "gmail.com"} # these entries are in some drop downs
    # Check if the content is already in the CSV file
    new_entries = []
    for content in contents:
        if content not in existing_entries and content not in excluded_entries and len(content) > 1:
            new_entries.append([content, source, current_date])

    # Append new entries to the CSV file
    if new_entries:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_entries)
        print(f"Contents successfully appended to {file_path}")
    else:
        print(f"All contents already exist in {file_path}")


# for updating the existing content with sources
def save_list_to_csv(contents, source, file_path):
    current_date = datetime.now().strftime('%Y-%m-%d')
    contents = filter_content(contents)
    
    # Read existing entries from the CSV file to check for duplicates
    existing_entries = {}
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    existing_entries[row[0]] = row[1:]

    excluded_entries = {"INACTIVE SOON:", "Random domain", "INACTIVE SOON", "gmail.com"}  # entries to exclude
    new_entries = []
    updated_lines = []
    updated = False

    for content in contents:
        if content in excluded_entries or len(content) <= 1:
            continue
        
        if content not in existing_entries:
            new_entries.append([content, source, current_date])
        else:
            row = existing_entries[content]
            if row[0] != source:
                while len(row) < 2:
                    row.append('')
                row[0] = source
                row[1] = current_date
                updated = True
            updated_lines.append([content] + row)

    # Write all updated lines back to the file
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write updated existing entries
        for key, value in existing_entries.items():
            if key not in [entry[0] for entry in new_entries]:  # Avoid duplication
                writer.writerow([key] + value)
        # Write new entries
        writer.writerows(new_entries)
    
    if new_entries:
        print(f"New contents successfully appended to {file_path}")
    if updated:
        print(f"Some contents updated with new source and date in {file_path}")
