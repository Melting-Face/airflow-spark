from datetime import datetime

from configs import AIRFLOW_HOME, spark_confs

from airflow.decorators import dag
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

    spark_submit


spark_submit_dag()
