import requests
URL = "https://www.whitehouse.gov/about-the-white-house/presidents/"
#print(requests.get(URL).text)
html_doc = requests.get(URL).text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup.find_all(class_="acctext--con grid-item__title h4alt"):
  print(tag.text.strip())
