from time import sleep

from airflow.decorators import dag, task

from datetime import datetime

@dag(
        dag_id="meu_pipeline",
        description="Um pipeline simples usando Airflow",
        schedule="****",
        start_date=datetime(2024, 1, 1),
        catchup=False
)
def pipeline():

    @task
    def primeiro_atividade():
        print("Executando a primeira atividade")
        sleep(2)

    @task
    def segunda_atividade():
        print("Executando a segunda atividade")
        sleep(2)

    @task
    def terceira_atividade():
        print("Executando a terceira atividade")
        sleep(2)


    primeiro_atividade()
    segunda_atividade()
    terceira_atividade()

pipeline()