import requests
from bs4 import BeautifulSoup
import json
import time
import random

# Set the User-Agent header to a browser-like string to avoid being blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}

# Send a request to the website to get the phone details
phoneDetails = requests.get(
    "https://www.gsmarena.com/samsung_galaxy_a14-12151.php", headers=headers)

# Wait for a random time between 1-3 seconds before sending the next request
time.sleep(random.uniform(1, 3))

# Create empty lists to store the phone information and specifications
information = []
specifications = []

# Use BeautifulSoup to parse the HTML response and extract the information and specifications
soup = BeautifulSoup(phoneDetails.text, 'html.parser')
for header in soup.find_all('td', class_="ttl"):
    information.append(header.get_text())
for specs in soup.find_all('td', class_="nfo"):
    specifications.append(specs.get_text())

# Combine the information and specifications into a dictionary
phoneSpec = dict(zip(information, specifications))

# Write the dictionary to a JSON file named "output.json"
with open("output.json", "w") as outfile:
    json.dump(phoneSpec, outfile)

# Print a message indicating that the scraping is complete
print(
    f"Scraping of {phoneSpec['Models']} Phone specifications Complete! Enjoy!")
