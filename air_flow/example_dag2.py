from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import mlflow
import hydra
import os
from omegaconf import DictConfig
import json


# Get the directory where the DAG file resides
DAG_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = "/mnt/e/projects/stock_prices/stock_predictor"
# Set the working directory to the project root directory
os.chdir(PROJECT_ROOT_DIR)

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

# This automatically reads in the configuration
@hydra.main(version_base= None , config_path='.' , config_name='config')
def data_ingestion(config: DictConfig):
    # Setup the wandb experiment. All runs will be grouped under this name
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    _ = mlflow.run(
        os.path.join(hydra.utils.get_original_cwd(),
                        "src",
                        "data_ingestion"),
        "main",
        env_manager="local",
        parameters={
            "stock_name": config["data_ingestion"]["stock_name"],
            "start_date": config["data_ingestion"]["start_date"],
            "end_date": config["data_ingestion"]["end_date"],
            "output_artifact": config["data_ingestion"]["stock_name"],
            "output_type": "raw_data",
            "output_description": "Stock raw data"
        },
    )
    
# Define the DAG
dag = DAG(
    'test_dag',
    default_args=default_args,
    description='A simple DAG example',
    schedule_interval=timedelta(days=1),  # Run daily
)

task_1 = BashOperator(
    task_id='change environment',
    bash_command='conda activate stock_predictor',
    dag=dag,
)

task_2 = BashOperator(
    task_id='change directory',
    bash_command='/mnt/e/projects/stock_prices/stock_predictor',
    dag=dag,
)

task_3 = BashOperator(
    task_id='Execute data injestion',
    bash_command='mlflow run . --env-manager local',
    dag=dag,
)

task_1 >> task_2 >> task_3
