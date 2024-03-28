from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 20),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'my_first_dag',
    default_args=default_args,
    description='A simple DAG example',
    schedule_interval=timedelta(days=1),  # Run daily
)

# Task 1: Print current date
task_1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Task 2: Sleep for 5 seconds
task_2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,  # Retry this task 3 times upon failure
    dag=dag,
)

# Task 3: Print "Done"
task_3 = BashOperator(
    task_id='print_done',
    bash_command='echo "Done"',
    dag=dag,
)

# Define task dependencies
task_1 >> task_2 >> task_3
