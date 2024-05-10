import os
import requests
import re
import sys

def get_spreadsheet_id(url):
    # Extract the spreadsheet ID from the URL
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", url)
    if match:
        return match.group(1)
    return None

def get_sheets_metadata(spreadsheet_id):
    # Retrieve the metadata to identify the sheet names and GIDs
    API_KEY = "AIzaSyCN61atZfVyU79LlijBlz-YKsXK6G7ys4M"
    url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}?key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sheets = data.get('sheets', [])
        # Extract title and GID for each sheet
        return [(sheet['properties']['title'], sheet['properties']['sheetId']) for sheet in sheets]
    else:
        print(f'Error retrieving sheet metadata: {response.status_code}')
        sys.exit(1)

def download_sheet(spreadsheet_id, gid, sheet_title):
    # Download a specific sheet using the GID
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}'
    response = requests.get(url)
    if response.status_code == 200:
        # Create a safe file name based on the sheet title
        outFile = re.sub(r'\W+', '_', sheet_title) + ".csv"
        filepath = os.path.join(os.getcwd(), outFile)
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print(f'CSV file saved to: {filepath}')
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')

# Main script
spreadsheet_url = input("Enter the URL: ")
spreadsheet_id = get_spreadsheet_id(spreadsheet_url)

if spreadsheet_id:
    # Get sheet metadata to know which sheets exist and their GIDs
    sheets_metadata = get_sheets_metadata(spreadsheet_id)
    for sheet_title, gid in sheets_metadata:
        download_sheet(spreadsheet_id, gid, sheet_title)
else:
    print("Invalid URL or spreadsheet ID not found.")

sys.exit(0)  # Success
