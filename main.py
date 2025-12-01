from time import sleep

def primeiro_atividade():
    print("Executando a primeira atividade")
    sleep(2)

def segunda_atividade():
    print("Executando a segunda atividade")
    sleep(2)

def terceira_atividade():
    print("Executando a terceira atividade")
    sleep(2)

def pipeline():
    primeiro_atividade()
    segunda_atividade()
    terceira_atividade()

pipeline()