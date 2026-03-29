import requests
from scrapy import *
from requests import *

class WebScraper(Spider):
    def __init__(self,url,name):
      self.url = url
      self.name = name
    def start_requests(self):
        urls=self.url
        for url in urls:
            yield Request(url,callback=self.parse)
    def parse(self,response):

        branch=response.css('p.block font-semibold text-gray-800 text-4xl md:text-5xl lg:text-6xl dark:text-gray-200 w-fit whitespace-nowrap text-center lg:text-left ::text')

        with open(file) as f:
            f.write(branch)







