#Beautiful Soap 4
import requests
from bs4 import BeautifulSoup

movie = input("Enter Movie Name: ")

word_list = list(movie.split(" "))

search_movie = ""
for words in word_list:
    search_movie = search_movie + "%20" + words
search_movie = search_movie[3:]

search_link = "https://yts.mx/browse-movies/" + search_movie + "/all/all/0/latest/0/all"

r = requests.get(search_link)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')

anchor = soup.find("a", class_ = "browse-movie-link")
url = anchor.get("href")
# print(url)

r2 = requests.get(url)
htmlcontent2 = r2.content
soup2 = BeautifulSoup(htmlcontent2, 'html.parser')
# print(soup2.title)
torrent_links = soup2.find("p", class_ ="hidden-md hidden-lg")
import re

a = torrent_links.find_all("a")
for item in a:
    print(item.get_text())
    print(item.get("href"))