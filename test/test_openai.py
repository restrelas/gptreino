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
idade = 20
tipo_treino = ["Treino cardiovascular", "Treino de definição", "Treino de força", "Treino funcional", "Treino de hipertrofia", "Treino leve"]
divisao_treino = ['ABC', 'ABCD', 'ABCDE']
condicao_med = ["doença cardíaca", "asma ou doença respiratória", "gravidez", "nenhum"]
nivel_atual = ["sendentaria", "moderada", "ativo"]
peso = 50
altura = 1.65


dadosPessoais = utils.get_dados_pessoais(nome, sexo[0], idade, peso, altura, tipo_treino[0], divisao_treino[1], condicao_med[3], nivel_atual[0])
print(dadosPessoais)
inicio = time.time()
response = main.conversation(dadosPessoais)
fim = time.time()


print(response)
print("\ntempo: ", fim - inicio)

utils.generate_csv(response)
print("\nArquivo CSV criado")