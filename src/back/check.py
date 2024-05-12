import requests
from bs4 import BeautifulSoup
import urllib
import sys
from urllib.parse import urlparse

url = sys.argv[1]  # Recuperer le lien du site web
response = requests.get(url)
i = 0
doutes = 0
#contient 
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        i+=1
        # href = link.get('href')
        # text = link.text
        # print(text, href)
        # Traitez le contenu HTML ici
    if (i < 2):
        doutes += 1
else:
    print("La requête a échoué avec le code d'état :", response.status_code)

parsed_url = urlparse(url)
base_url = parsed_url.scheme + "://" + parsed_url.netloc
if (parsed_url.scheme == "http"):
    doutes += 1
