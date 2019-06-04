# Climate Investment Fund Web Scraping Project

This application scrapes open source data from an API on the Word Bank website. This is cleansed prior to saving to a MongoDB database with help of the pymongo library. The database is queried for certain fields in order to produce panda dataframes. Dataframes are use to produce three summary reports on Clean Technology Fund investment ($M USD) across countries, regions and various technological focuses. 

##Running the application

The application should be configured to run from the app.py file.
Please ensure to install the 'requirements.txt' file.
Keeping in mind best practice, should you choose to modify the file

##Data Set Information

Dataset name: 2018 Climate Investment Funds - Clean Technology Fund (CTF)
Data relates to the World Bank Group Finance's portfolio on CTF projects across 4 regions. 

Further information on fields in data set:
https://finances.worldbank.org/Projects/2018-Climate-Investment-Funds-Clean-Technology-Fun/kjmm-jfbk

Disclaimer: I have chose to work with this dataset for educational purposes. Should you choose to scrape the API specified within this project, this is at your own risk and liability. Thus please read terms and conditions for working with the open source data set. 