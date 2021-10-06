# import requests
# URL = "https://www.whitehouse.gov/about-the-white-house/presidents/"
# html_doc = requests.get(URL).text
html_doc = """
<ol style="list-style-type: decimal">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: decimal-leading-zero">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>
 
<ol style="list-style-type: upper-roman">
  <li class="elements">Élément1</li>
  <li class="elements">Élément2</li>
  <li class="elements">Élément3</li>
</ol>

<ol style="list-style-type: lower-roman">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: upper-alpha">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: lower-alpha">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>

<ol style="list-style-type: lower-greek">
  <li>Élément</li>
  <li>Élément</li>
  <li>Élément</li>
</ol>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
for tag in soup.find_all(class_="elements"):
    print(tag.name+" "+tag.string)
#print(soup.find_all(class_="elements"))
#print(soup.get_text())