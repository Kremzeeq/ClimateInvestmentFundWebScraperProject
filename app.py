from web_scraper import CTFWebScraper
from database import Database

# Set constants for the database name (DB) and also collection (COLL)
DB_NAME = 'climate_investment_fund_2018'
COLL_CLEAN_TECH_FUNDS = 'clean_tech_funds'

# World Bank website provides link to API with data set available in json format
WEB_URL = "https://finances.worldbank.org/resource/kjmm-jfbk.json"
ctf_web_scraper = CTFWebScraper(WEB_URL)
clean_tech_funds = ctf_web_scraper.execute()

# Initialize DB Client
Database.initialize(DB_NAME)

# Insert scraped clean_tech_funds into the database
Database.insert_many(COLL_CLEAN_TECH_FUNDS, clean_tech_funds)

