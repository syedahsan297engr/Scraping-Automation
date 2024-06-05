from bs4 import BeautifulSoup
import requests

# URL of the webpage you want to scrape
url = 'https://verifymail.io/domain/promail9.net'

# Send a GET request to fetch the raw HTML content
response = requests.get(url)
web_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')

# Use CSS selectors to locate the specific section
div = soup.select_one('body > div:nth-of-type(3) > section:nth-of-type(2) > div:nth-of-type(1) > div > div > div:nth-of-type(1) > div > div:nth-of-type(2) > div:nth-of-type(6) > span')

# Fetch all <a> tags within the specified section
a_tags = div.find_all('a')

# Extract the content (text) of each <a> tag
a_texts = [a.get_text() for a in a_tags]

print(type(a_texts))
