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
   start_date=datetime(2026, 6, 21),
   schedule_interval='@weekly',
   catchup=False
 ) as dag:
   
   def extract_and_store():
      data = extract_data()
      store_raw_data(data)

   extract_store = PythonOperator(
      task_id='extract_store_data',
      python_callable=extract_and_store,
   )

   load = PythonOperator(
      task_id='load_data',
      python_callable=load_data,
   )

   extract_store >> load