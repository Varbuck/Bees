"""
### Spark Submit Example DAG
Esta DAG demonstra como submeter um job Spark usando o SparkSubmitOperator.
"""

from __future__ import annotations

import pendulum

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

# Definir argumentos padrão
default_args = {
    "owner": "airflow",
    "retries": 2,
}

# Instanciar a DAG
with DAG(
    dag_id="spark_submit_example_dag",
    default_args=default_args,
    description="DAG de exemplo para submeter um job Spark",
    schedule=None,  # Defina o agendamento conforme necessário
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example", "spark"],
) as dag:
    dag.doc_md = __doc__

    # Definir a tarefa que submete o job Spark
    spark_submit_task = SparkSubmitOperator(
        task_id="spark_submit_task",
        application="/opt/bitnami/airflow/dags/spark_app.py",  # Caminho para o aplicativo Spark
        conn_id="spark_default",
        name="spark_submit_example_job",
        verbose=True,
        conf={
            "spark.master": "spark://spark-master:7077",
            "spark.app.name": "SparkSubmitExample",
        },
    )

    # Definir a ordem das tarefas (se houver mais)
    spark_submit_task
