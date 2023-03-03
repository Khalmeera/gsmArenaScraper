# Phone Scraper

This script scrapes the phone details from a website and writes them to a JSON file. It uses the `requests` library to send HTTP requests to the website, `BeautifulSoup` to parse the HTML response, and `json` to write the phone details to a file.

## Installation

To run this script, you need to have [Python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/) installed on your system.

1. Clone the repository: 
```bash
git clone https://github.com/Khalmeera/gsmArenaScraper.git
```
2. Navigate to the project directory: 
```bash
cd gsmarenascraper
```
3. Install the dependencies: 
```bash
py -m pipenv install
```

## Usage

To run the script, use the following command: 
```bash
py -m pipenv run python .\scraper.py
```

The script will scrape the phone details from the website and write them to a file named `output.json`. The script also adds a random delay between requests to avoid getting blocked by the website.