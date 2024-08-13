from pyspark.sql import DataFrame as D
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("SparkExample")
    .enableHiveSupport()
    .getOrCreate()
)

df: D = spark.createDataFrame(
    [
        (1, "John Doe", 21),
        (2, "Jane Doe", 22),
        (3, "Joe Bloggs", 23),
    ],
    ["id", "name", "age"],
)

result = (
    df.write.mode("overwrite")
    .option("path", "s3a://warehouse/abcde")
    .format("parquet")
    .saveAsTable("default.abcde")
)
