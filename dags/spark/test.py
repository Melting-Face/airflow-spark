from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("SparkExample")
    .enableHiveSupport()
    .config("hive.default.fileformat", "parquet")
    .config("spark.sql.session.timeZone", "Asia/Seoul")
    .config("spark.speculation", "true")
    .getOrCreate()
)

df = spark.createDataFrame(
    [
        (1, "John Doe", 21),
        (2, "Jane Doe", 22),
        (3, "Joe Bloggs", 23),
    ],
    ["id", "name", "age"],
)
df.show()
