import csv
import time

def get_dados_pessoais(nome, sexo, idade, peso, altura, objetivo, dias, condicao_med, nivel_atual):
    
    info = {
        "nome": nome,
        "sexo": sexo,
        "idade": idade,
        "peso": peso,
        "altura (em cm)": altura,
        # "imc": peso/((altura/100)**2),
        "objetivo": objetivo,
        "dias": dias,
        "condicao medica": condicao_med,
        "nivel atual de atividades": nivel_atual

    }
    return info

def generate_csv(str):
    nome_arquivo = "ficha_tecnica.csv"

    linhas = str.strip().split('\n')

    dados = []
    for linha in linhas:
        dados.append(linha.strip().split(','))

    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(dados)
