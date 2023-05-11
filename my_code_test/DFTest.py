from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("DFTest")\
        .getOrCreate()
    
    df = spark.read.format("csv").load("data/recovery.csv")

    df.show(5)
