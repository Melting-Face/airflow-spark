import os

AIRFLOW_HOME = os.environ["AIRFLOW_HOME"]

spark_confs = {
    "spark.master": "spark://spark:7077",

    "spark.jars": "/opt/airflow/jars/*",

    # DataNucleus가 테이블이 존재하지 않는 경우 자동으로 테이블을 생성
    "spark.hadoop.datanucleus.autoCreateTables": True,
    # DataNucleus가 테이블/스키마 존재하지 않는 경우 테이블/스키마 자동으로 생성
    "spark.hadoop.datanucleus.schema.autoCreateTables": True,
    # DataNucleus가 사용하는 데이터 스토어(데이터베이스 구조)가 고정되지 않음
    "spark.hadoop.datanucleus.fixedDatastore": False,

    "spark.hadoop.fs.s3a.access.key": "admin",
    "spark.hadoop.fs.s3a.secret.key": "admin1234",
    "spark.hadoop.fs.s3a.endpoint": "http://minio:9000",
    "spark.hadoop.fs.s3a.path.style.access": True,
    "spark.hadoop.fs.s3a.connection.ssl.enabled": False,
    "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
    "spark.driver.userClassPathFirst": True,
    "spark.sql.warehouse.dir": "s3a://warehouse",
    "spark.sql.parquet.int96TimestampConversion": "true",
    "spark.sql.parquet.mergeSchema": "true",
    "spark.sql.parquet.compression.codec": "gzip",
    "spark.sql.session.timeZone": "Asia/Seoul",
    "spark.sql.extensions": "io.delta.sql.DeltaSparkSessionExtension",
    "spark.sql.catalog.spark_catalog": "org.apache.spark.sql.delta.catalog.DeltaCatalog",
}
