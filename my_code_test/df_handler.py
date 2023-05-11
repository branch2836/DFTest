import requests
from pyspark.sql import *


class DfHandler:

    def __init__ (self):
        self.spark = SparkSession\
            .builder\
            .master("local[3]")\
            .appName("DfTest")\
            .getOrCreate()

    def get_df_from_api(self, url, payload):
        return requests.get(url, params=payload)