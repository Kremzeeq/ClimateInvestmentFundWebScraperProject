from pymongo import MongoClient
from web_scraper import CTFWebScraper

# Set constants for the database name (DB) and also collection (COLL)
DB_CLIMATE_INVESTMENT_FUND_2018 = 'climate_investment_fund_2018'
COLL_CLEAN_TECH_FUNDS = 'clean_tech_funds'

def get_mongo_db(db_name, host ='localhost',
                 port=27017, username=None, password=None):
    # make Mongo connection with/out authenication
    if username and password:
        mongo_uri = 'mongodb://{}:{}@{}{}'.format(username, password,
                                                  host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db_name]

db = get_mongo_db(DB_CLIMATE_INVESTMENT_FUND_2018)
coll = db[COLL_CLEAN_TECH_FUNDS]

# World Bank website provides link to API with data set available in json format
WEB_URL = "https://finances.worldbank.org/resource/kjmm-jfbk.json"
ctf_web_scraper = CTFWebScraper(WEB_URL)
clean_tech_funds = ctf_web_scraper.execute()
coll.insert_many(clean_tech_funds)