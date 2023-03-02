import requests
from bs4 import BeautifulSoup
import json
import time
import random

base = ('https://www.gsmarena.com/')
makers = requests.get('https://www.gsmarena.com/makers.php3')

soup = BeautifulSoup(makers.text, 'html.parser')

manufacturerList = []
phoneList = []

print("Scraping of GSM Arena Phone URLs is in progress, kindly wait for 5 minutes. To terminate, press CTRL + C. You will get a json file containing the URLs shortly")

for link in soup.find_all('div', class_="st-text"):
    for a in link.find_all('a', href=True):
        manufacturerList.append(base+a['href'])

for manufacturer in manufacturerList:

    time.sleep(random.randint(1, 3))

    phonesForEachManufacturer = requests.get(manufacturer)
    soup = BeautifulSoup(phonesForEachManufacturer.text, 'html.parser')

    try:
        numPages = len(soup.find_all(
            'div', class_='nav-pages')[0].find_all('a'))
    except IndexError:
        numPages = 1

    for pageNum in range(1, numPages+1):

        manufacturerId = manufacturer.split('-')[2].split('.')[0]

        if pageNum == 1:
            url = manufacturer
        else:
            url = f"{manufacturer[:-4]}-f-{manufacturerId}-0-p{pageNum}.php"

        time.sleep(random.randint(2, 4))
        page = requests.get(url)
        soupPage = BeautifulSoup(page.text, 'html.parser')

        for phoneLink in soupPage.find_all('div', class_="makers"):
            for a in phoneLink.find_all('a', href=True):
                phoneList.append(base+a['href'])

with open("output.json", "w") as outfile:
    json.dump(phoneList, outfile)

print("Done! I have found: "+str(len(phoneList)) +
      " urls, you can find the json file in the script directory. Have fun!")
