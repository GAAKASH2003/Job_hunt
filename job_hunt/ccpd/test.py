from requests_html import HTMLSession
import json
import requests
import requests
from bs4 import BeautifulSoup
def oncamp():
    url = "https://www.xpiria.in/placement"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
oncamp()    