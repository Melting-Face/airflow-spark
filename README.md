# airflow with spark 

```
hive.metastore.uris                                thrift://hive:9083

spark.master                                       spark://spark:7077

spark.sql.extensions                               io.delta.sql.DeltaSparkSessionExtension
spark.sql.catalog.spark_catalog                    org.apache.spark.sql.delta.catalog.DeltaCatalog
spark.sql.warehouse.dir                            s3a://warehouse
spark.sql.hive.metastore.warehouse.dir             s3a://warehouse

spark.hadoop.datanucleus.autoCreateTables          true
spark.hadoop.datanucleus.schema.autoCreateTables   true
spark.hadoop.datanucleus.fixedDatastore            false

spark.hadoop.fs.s3a.access.key                     admin
spark.hadoop.fs.s3a.secret.key                     admin1234
spark.hadoop.fs.s3a.endpoint                       http://minio:9000
spark.hadoop.fs.s3a.path.style.access              true
spark.hadoop.fs.s3a.connection.ssl.enabled         false
spark.hadoop.fs.s3a.impl                           org.apache.hadoop.fs.s3a.S3AFileSystem
```
