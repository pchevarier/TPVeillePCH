import requests
import json

URL = "https://www.sirene.fr/sirene/public/recherche"
sheaders = headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2919.83 Safari/537.36'}

request = requests.get(URL , headers=sheaders)
gcookies = request.cookies
gheaders =  request.headers
gtext =  request.text
print ('COOKIES')
print(gcookies)
#scookies = json.dumps(gcookies)
print ('HEADERS')
print(gheaders)
#print ('HTML')
#print(gtext)
#html_doc = requests.post(URL,data="{'rechercheEntreprise':1,'communeQuery':'01000'}",cookies = gcookies , headers = gheaders )
data = {
  "recherche.sirenSiret":"",
  "recherche.raisonSociale":"a",
  "recherche.adresse":"",
  "recherche.commune":"",
  "recherche.captcha":"",
  "recherche.excludeClosed":True,
  "__checkbox_recherche.excludeClosed":True
  }

html_doc = requests.post(URL,data=data,cookies = gcookies )
print ("HTML2")
print (html_doc.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.text)
#for tag in soup.find_all(class_="acctext--con grid-item__title h4alt"):
#  print(tag.text.strip())
