import requests
from bs4 import BeautifulSoup


# Creating a class to make an HTTP GET request, handle HTTP errors and return parsed HTML
class Scraper:
    def __init__(self, headers):
        self.headers = headers

    # Scraping MyHome pages based on index
    def scrape_page(self, ind):
        url = (f'https://www.myhome.ge/ka/s/?Keyword=თბილისი&AdTypeID=1&Page={ind}&SortID=1&mapC=41.73188365%2C44.8368762993663&cities=1996871&GID=1996871')

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "lxml")
            return soup
        except requests.exceptions.HTTPError as http_err:
            return f"Error: Unable to retrieve data. Status code: {http_err.response.status_code}"

    # Scraping each advertisement page
    def scrape_advertisement(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "lxml")
            return soup
        except requests.exceptions.HTTPError as http_err:
            return f"Error: Unable to retrieve data. Status code: {http_err.response.status_code}"
