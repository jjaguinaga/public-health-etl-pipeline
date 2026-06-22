from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/Users/naga/Desktop/public-health-etl-pipeline')
from extract import extract_data, store_raw_data
from load import load_data

with DAG(
   dag_id='public_health_pipeline',
   description='ETL pipeline for CDC COVID vaccine effectiveness data',
   start_date=datetime(2026, 1, 1),
   schedule_interval='@weekly',
   catchup=False
 ) as dag:
   
   extract = PythonOperator(
      task_id='extract_data',
      python_callable=extract_data
   )
   
   store_raw = PythonOperator(
      task_id='store_raw_data',
      python_callable=store_raw_data
   )
   
   load = PythonOperator(
      task_id='load_data',
      python_callable=load_data
   )
   
   extract >> store_raw >> load