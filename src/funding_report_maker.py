import pandas as pd
import os
from os import path
import shutil

class FundingReportMaker():
    def __init__(self, database, collection):
        self.database = database
        self.collection = collection

    def execute(self):
        df = self.get_db_funding_df()
        self.reset_reports_dir()
        self.generate_reports(df)

    def get_db_funding_df(self):
        cursor = self.database.find_and_spec_columns(self.collection,{"year":2018},
                                                     {"region": 1, "country": 1,
                                                      "technology_focus": 1, "ctf_funding_usd": 1})
        df = pd.DataFrame(list(cursor))
        return df

    def generate_reports(self, df):
        report_levels = ['region', 'country','technology_focus']
        for report_level in report_levels:
            self.get_report(df, report_level)
            self.provide_report_overview(df, report_level)

    def get_report(self, df, report_level):
        """
        :param df: Pandas dataframe
        :param report_level: can be a field, e.g. region, country, technology focus
        :return: report in /reports directory, in relation to the defined report_level
        """
        # provides summary statistics based on ctf_funding_usd
        summary_df = df.groupby(report_level).describe().round(2)
        print(summary_df)
        file_name = 'reports/'+report_level+'_report.csv'
        title = "Funding Report: By {}, Metric: CTF Funding $(USD)m".format(report_level)
        with open(file_name, 'a') as f:
            f.write("{} \n".format(title))
            summary_df.to_csv(f)

    def reset_reports_dir(self):
        """
        Remakes reports directory and removes pre-exiting reports
        """
        try:
            shutil.rmtree('reports/')
        except OSError as e:
            print("Error: {}. /reports directory does not exist".format(e))
        os.mkdir('reports/')

    def provide_report_overview(self, df, report_level):
        """
        Provides a mini report to the console on highest mean values for the report_level
        """
        ctf_mean_df = df.groupby(report_level).mean()['ctf_funding_usd'].round(2)
        #idxmax identifies the index value for the report_level with the highets mean value
        report_level_highest_mean = ctf_mean_df.idxmax()
        highest_mean_funding = ctf_mean_df.max()
        print("The {} with the highest mean funding for CTF World Bank CTF projects is {} with ${}m (USD) ".
              format(report_level, report_level_highest_mean, highest_mean_funding))
