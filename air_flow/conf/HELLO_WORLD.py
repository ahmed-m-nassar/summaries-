from __future__ import annotations

import pendulum
from pprint import pprint
from datetime import timedelta
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "nassar",
    "start_date": pendulum.now(),
    "depends_on_past": False,
    "retries": 3,
    "email_on_retry": False,
    "retry_delay": timedelta(minutes=5),
    "catchup": False
}

@dag(
    default_args=default_args,
    description='Print Hello World',
    schedule_interval='@daily'
)
def hello_world():
    
    def print_context(**kwargs):
        """Print the Airflow context and ds variable from the context."""
        pprint(kwargs)
        return "Hellow World!!!"
    
    print_context_task = PythonOperator(
        task_id='print_context',
        python_callable=print_context
    )

    print_context_task

hello_world_dag = hello_world()
