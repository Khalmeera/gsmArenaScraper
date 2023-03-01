import requests
from bs4 import BeautifulSoup
import json
import time
import random

makers = requests.get('https://www.gsmarena.com/makers.php3')

soup = BeautifulSoup(makers.text, 'html.parser')


for link in soup.find_all('div', class_="st-text"):
    for a in link.find_all('a', href=True):
        time.sleep(random.randint(2, 8))
        print(a['href'])
