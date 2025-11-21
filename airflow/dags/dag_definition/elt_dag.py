from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.redshift_sql import RedshiftSQLExecuteQueryOperator
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from src.extract_to_s3 import extract_and_load_to_s3
from airflow.models import Variable


BUCKET = "shopease-datalake"

default_args = {
    "owner": "PrimeCart",
    "retries": 2,
}
dag = DAG(
    dag_id="elt_sales_data_pipeline",
    description="Write files to s3, transform with databricks, load to redshift",
    start_date=datetime(2025, 11, 21),
    schedule="0 4 * * *",
    catchup=False,
    default_args=default_args,
    tags=["bronze", "extract"],
)

write_raw_data = PythonOperator(
    task_id="write_raw_data_to_s3",
    python_callable=extract_and_load_to_s3,
    dag=dag,
)

transform_data = DatabricksSubmitRunOperator(
    task_id="transform_data_with_databricks",
    databricks_conn_id="databricks_default",
    job_id=Variable.get("databricks_job_id"),
    #66628683160877,
    dag=dag,
)

load_to_redshift = RedshiftSQLExecuteQueryOperator(
    task_id="load_Summarised_data_to_redshift",
    redshift_conn_id="redshift_default",
    sql="src/copy.sql",
    dag=dag,
)

write_raw_data >> transform_data >> load_to_redshift