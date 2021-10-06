import requests
URL = "https://www.whitehouse.gov/about-the-white-house/presidents/"
#print(requests.get(URL).text)
html_doc = requests.get(URL).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)
print(soup.find_all("span",class_="screen-reader-text").string())