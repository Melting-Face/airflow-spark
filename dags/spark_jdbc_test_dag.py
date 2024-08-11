from datetime import datetime

from configs import AIRFLOW_HOME, spark_confs

from airflow.decorators import dag
from airflow.providers.apache.spark.operators.spark_jdbc import SparkJDBCOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


@dag(
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    tags=["test"],
    catchup=False,
)
def spark_submit_dag():
    spark_submit = SparkSubmitOperator(
        task_id="spark_submit",
        conn_id="spark_conn_id",
        conf=spark_confs,
        application=f"{AIRFLOW_HOME}/dags/spark/test.py",
    )

    jdbc_to_spark = SparkJDBCOperator(
        task_id="jdbc_to_spark",
        spark_conn_id="spark_conn_id",
        spark_conf=spark_confs,
        cmd_type="jdbc_to_spark",
        jdbc_conn_id="mysql_jdbc_conn_id",
        jdbc_driver="com.mysql.cj.jdbc.Driver",
        jdbc_table="dag",
        metastore_table="dag",
        save_format="parquet",
        save_mode="overwrite",
    )

    jdbc_to_spark

    spark_submit

spark_submit_dag()
