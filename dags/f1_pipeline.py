from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="f1_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    # 1. scrape the data and save it as csv files
    extract = BashOperator(
        task_id="extract",
        bash_command="cd /opt/airflow/EL && python extract.py",
    )

    # 2. load the csv files into postgres (raw tables)
    load = BashOperator(
        task_id="load",
        bash_command="cd /opt/airflow/EL && python load.py",
    )

    # 3. run the dbt models
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/T && dbt run --profiles-dir .",
    )

    # 4. run the dbt tests
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/T && dbt test --profiles-dir .",
    )

    extract >> load >> dbt_run >> dbt_test
    