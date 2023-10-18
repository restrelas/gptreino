import csv

def get_dados_pessoais(nome, sexo, idade, objetivos, peso, altura, dias):
    info = {
        "nome": nome,
        "sexo": sexo,
        "idade": idade,
        "objetivos": objetivos,
        "peso": peso,
        "altura": altura,
        "imc": peso/(altura**2),
        "dias": dias
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
