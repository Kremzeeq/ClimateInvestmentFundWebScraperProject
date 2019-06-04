
"""
This module scrapes a json file from an API on the Word Bank website
Dataset name: 2018 Climate Investment Funds - Clean Technology Fund (CTF)
Data relates to the World Bank Group Finance's portfolio on CTF projects across 4 regions
Further information:
https://finances.worldbank.org/Projects/2018-Climate-Investment-Funds-Clean-Technology-Fun/kjmm-jfbk

"""
import requests
import ast
import uuid
from fields_with_nums import fields_with_nums

class WebScraper():
    def __init__(self, web_url):
        self.web_url = web_url

    def get_page_content(self):
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

class CTFWebScraper(WebScraper):
    def __init__(self, web_url):
        WebScraper.__init__(self, web_url)

    def execute(self):
        page_content = self.get_page_content()
        decoded =  self.get_list_of_jsons(page_content)
        return self.clean(decoded)

    def get_list_of_jsons(self, page_content):
        #decode bytes to string object
        decoded = page_content.decode('UTF-8')
        # ast.literal_eval evaluates a string object and can return python literal structures
        decoded = ast.literal_eval(decoded)
        print("Decoded")
        print(decoded)
        print(type(decoded))
        return decoded

    def clean(self, decoded):
        for doc in decoded:
            self.update_doc(doc)
        print("Now cleaned")
        return decoded

    def update_doc(self, doc):
        doc = self.convert_string_fields_to_int(doc, fields_with_nums)
        doc['_id'] = uuid.uuid4().hex
        doc['year'] = doc.pop('ry')
        if doc['region'] == "Europe and Central Asisa":
            doc['region'] = "Europe and Central Asia"

        return doc

    def convert_string_fields_to_int(self, doc, fields_with_nums):
        for k in doc.keys():
            if k in fields_with_nums:
                doc[k] = float(doc[k])
        return doc