import time
import sys
import os

current_directory = os.path.dirname(__file__)
project_directory = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.append(project_directory)

import utils
import main

# entrada
nome = "Fulano"
sexo = ["feminino", "masculino"]
idade = 14 
objetivo = ["perda de peso", "ganho de massa muscular", "melhoria da resistência cardiovascular","melhoria de flexibilidade", "melhoria de postura", "alívio de dores crônicas", "treinamento funcional"]
dias = 4
condicao_med = ["doença cardíaca", "diabete", "asma ou doença respiratória", "obesidade", "gravidez", "nenhum"]
nivel_atual = ["sendentaria", "moderada", "ativo"]
peso = 45
altura = 1.65


dadosPessoais = utils.get_dados_pessoais(nome, sexo[0], idade, peso, altura, objetivo[0], dias, condicao_med[5], nivel_atual[0])
print(dadosPessoais)
inicio = time.time()
response = main.conversation(dadosPessoais)
fim = time.time()


print(response)
print("\ntempo: ", fim - inicio)

utils.generate_csv(response)
print("\nArquivo CSV criado")