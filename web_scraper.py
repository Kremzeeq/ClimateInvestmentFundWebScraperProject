from bs4 import BeautifulSoup as bs
import requests
"""
This module scrapes a table from The Word Bank website
Table Name: 2018 Climate Investment Funds - Clean Technology Fund (CTF)
Data relates to the World Bank Group Finance's portfolio on CTF projects across 4 regions


"""

class WebScraper():
    def __init__(self, web_url):
        self.web_url = web_url

    def execute(self):
        page = self.get_request()
        if page['success'] == True:
            print(page['context'].content)
            return page['context'].content

    def get_request(self):
        page = requests.get(self.web_url)
        if page.status_code == 200:
            print("Page successfully requested")
            return {"success": True, "context": page}
        else:
            outcome = "Request failed, status code: {}".format(page.status_code)
            print(outcome)
            return {"success": False, "context":outcome}

# World Bank website provides link to API with data set available in json format
WEB_URL = "https://finances.worldbank.org/resource/kjmm-jfbk.json"
web_scraper = WebScraper(WEB_URL)
web_scraper.execute()