import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.__url = url

    def scrape(self):
        response = requests.get(self.__url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()

    def scrape_to_file(self, filename):
        content = self.scrape()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)