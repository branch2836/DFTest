import requests
from pyspark.sql import *


class DfHandler:

    def __init__(self):
        self.spark = SparkSession \
            .builder \
            .master("local[3]") \
            .appName("DfTest") \
            .getOrCreate()

    def get_df_from_api(self, url, payload):
        r = requests.get(url, params=payload)
        response = r.text.split('\n')
        columns = response.pop(0).split(',')
        people = []
        for line in response:
            if len(line) > 10:
                people.append(tuple(line.split(',')))
        df = self.spark.createDataFrame(data=people, schema=columns)
        return df
