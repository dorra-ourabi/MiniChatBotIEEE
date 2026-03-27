from ChatClass import *
from bs4 import BeautifulSoup

from WebScraperClass import WebScraper


class HtmlScraper(WebScraper):
      def __init__(self,url,method):
          super().__init__(url)
          self._method = method
          def scrape(self):
                text=""
                """personalize your scraping code and return the extracted content in the variable text"""
                return text
