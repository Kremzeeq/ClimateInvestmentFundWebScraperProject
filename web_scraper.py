
"""
This module scrapes a json file from an API on the Word Bank website
Dataset name: 2018 Climate Investment Funds - Clean Technology Fund (CTF)
Data relates to the World Bank Group Finance's portfolio on CTF projects across 4 regions
Further information:
https://finances.worldbank.org/Projects/2018-Climate-Investment-Funds-Clean-Technology-Fun/kjmm-jfbk

"""
import requests
import ast
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
        return self.get_list_of_jsons(page_content)

    def get_list_of_jsons(self, page_content):
        #decode bytes to string object
        decoded = page_content.decode('UTF-8')
        # ast.literal_eval evaluates a string object and can return python literal structures
        decoded = ast.literal_eval(decoded)
        print(decoded)
        print(type(decoded))
        return decoded





#{"ry":"2018","project_title":"Concentrated Solar Power Project","country":"Chile","region":"Latin America and Caribbean","public_private":"Private","technology_focus":"Renewable Energy","specific_technology":"RE-Solar","ctf_funding_usd":"67","mdb_1":"IDB","lifetime_where_available":"30","expected_ghg_reductions_lifetime_tco2":"3879000","expected_ghg_reductions_annual_tco2_yr":"129300","expected_co_financing_total_us_m":"0","expected_co_financing_mdb1_us_m":"66","expected_co_financing_govt_us_m":"20","expected_co_financing_pvt_us_m":"130","expected_co_financing_bilateral_us_m":"143","expected_co_financing_others_us_m":"0","expected_installed_capacity_total_mw":"50","expected_installed_capacity_wind_mw":"0","expected_installed_capacity_solar_mw":"50","expected_installed_capacity_hydro_mw":"0","expected_installed_capacity_geothermal_mw":"0","expected_installed_capacity_mixed_mw":"0","expected_additional_passengers_upon_implementation_passengers_per_day":"0","expected_energy_savings_annual_gwh_yr":"0","actual_2015_ghg_reductions_annual_tco2_yr":"0","actual_2015_co_financing_total_us_m":"0","actual_2015_co_financing_mdb1_us_m":"0","actual_2015_co_financing_govt_us_m":"0","actual_2015_co_financing_pvt_us_m":"0","actual_2015_co_financing_bilateral_us_m":"0","actual_2015_co_financing_others_us_m":"0","actual_2015_installed_capacity_total_mw":"0","actual_2015_installed_capacity_wind_mw":"0","actual_2015_installed_capacity_solar_mw":"0","actual_2015_installed_capacity_hydro_mw":"0","actual_2015_installed_capacity_geothermal_mw":"0","actual_2015_installed_capacity_mixed_mw":"0","actual_2015_additional_passengers_upon_implementation_passengers_per_day":"0","actual_2015_energy_savings_annual_gwh_yr":"0","cumulative_ghg_reductions_annual_tco2_yr":"0","cumulative_co_financing_total_us_m":"0","cumulative_co_financing_mdb1_us_m":"0","cumulative_co_financing_govt_us_m":"0","cumulative_co_financing_pvt_us_m":"0","cumulative_co_financing_bilateral_us_m":"0","cumulative_co_financing_others_us_m":"0","cumulative_installed_capacity_total_mw":"0","cumulative_installed_capacity_wind_mw":"0","cumulative_installed_capacity_solar_mw":"0","cumulative_installed_capacity_hydro_mw":"0","cumulative_installed_capacity_geothermal_mw":"0","cumulative_installed_capacity_mixed_mw":"0","cumulative_additional_passengers_upon_implementation_passengers_per_day":"0","cumulative_energy_savings_annual_gwh_yr":"0","fund":"CTF"}